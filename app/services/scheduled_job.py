from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timezone
from app.core.firebase_init import db


async def run_alarms():
    print(f"Task executed at: {datetime.now()}")
    query = db.collection_group("alarms")
    alarms = query.stream()
    for alarm in alarms:
        # alarm.reference.parent == alarms
        # alarm.reference.parent.parent == device
        # alarm.reference.parent.parent.parent == user
        # print(alarm.id, alarm.get('dateTime'),
        #       alarm.reference.parent.parent.id,
        #       alarm.reference.parent.parent.parent.id,
        #       alarm.reference.parent.parent.parent.parent.id)
        alarm_id = alarm.id
        alaram_device_status = alarm.get('status')
        device_id = alarm.reference.parent.parent.id
        user_email = alarm.reference.parent.parent.parent.parent.id
        alarm_dict = alarm.to_dict()
        if alarm.get('dateTime') < datetime.now(timezone.utc) and (not ('executed' in alarm_dict) or alarm_dict.get('executed') == False):
            db.collection('users').document(user_email).collection('devices').document(device_id).update({
                'status': alaram_device_status,
            })
            db.collection('users').document(user_email).collection('devices').document(device_id).collection('alarms').document(alarm_id).update({
                'executed': True,
            })
            # 2. Set up the Lifespan to start/stop the scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize and start scheduler
    scheduler = AsyncIOScheduler()

    # Run every 60 seconds
    # scheduler.add_job(my_scheduled_task, "interval", seconds=60)

    # Or use Cron style: Every day at midnight
    scheduler.add_job(run_alarms, "cron", minute='*')

    scheduler.start()
    yield
    # Shutdown: Stop the scheduler
    scheduler.shutdown()

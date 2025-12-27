from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.device_controller import router
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.services.scheduled_job import lifespan

app = FastAPI(lifespan=lifespan)
origins = ["http://localhost:4200", "localhost"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router=router)

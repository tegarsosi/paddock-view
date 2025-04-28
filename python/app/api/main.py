from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.drivers import get_drivers_for_session
from app.enum.session_types import SessionType
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/drivers")
async def get_drivers(year: str, gp: str, session: str):
    drivers = get_drivers_for_session(int(year), gp, SessionType(session))
    return drivers

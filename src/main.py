from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI

from api.bets import bets_router
from api.dependencies import UOWDep
from api.events import events_router
from dto.events import AddEventDTO
from services.events import EventsService
from services.bets import BetService
from settings.config import settings_pg
from utils.unit_of_work import UnitOfWork


app = FastAPI()
app.include_router(bets_router)
app.include_router(events_router)

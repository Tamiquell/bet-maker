from fastapi import APIRouter, Depends

from api.dependencies import UOWDep
from dto.events import AddEventDTO, UpdateEventDTO, EventDTO
from services.events import EventsService
from services.bets import BetService

events_router = APIRouter(prefix="/events", tags=["Events"])


@events_router.patch("/{event_id}")
async def add_new_event(
        event_id: int,
        data: UpdateEventDTO,
        uow: UOWDep
):
    bet_service = BetService(uow)
    event_id = await EventsService(uow, bet_service).update_event(event_id, data)
    return event_id


@events_router.get("")
async def get_all_events(
    uow: UOWDep
) -> list[EventDTO]:
    bet_service = BetService(uow)
    all_events = await EventsService(uow, bet_service).get_events()
    return all_events

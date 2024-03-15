from dto.bets import UpdateBetDTO
from dto.events import AddEventDTO, EventDTO, UpdateEventDTO
from services.bets import BetService
from utils.unit_of_work import IUnitOfWork


class EventsService:

    def __init__(self, uow: IUnitOfWork, bets_service: BetService) -> None:
        self.uow = uow
        self.bets_service = bets_service

    async def get_events(self):
        async with self.uow:
            events = await self.uow.events.find_all()
            return events

    async def update_event(self, event_id: int, data: UpdateEventDTO):
        event_dict = data.model_dump(exclude_none=True)
        async with self.uow:
            # update event itself
            print(f"{event_dict=}")
            print(f"{event_id=}")

            # update all event's bets
            bets = await self.bets_service.get_bets(event_id)
            bets_ids = [bet.id for bet in bets]
            _ = await self.bets_service.update_bet(
                bets_ids,
                data=UpdateBetDTO(status=data.status)
            )

            updated_event = await self.uow.events.edit_one(
                id=event_id, data=event_dict)

            await self.uow.commit()
            return updated_event

    async def create_event(self, data: AddEventDTO):
        event_dict = data.model_dump()
        event_dict["status"] = "in process"
        async with self.uow:
            event_id = await self.uow.events.add_one(event_dict)
            await self.uow.commit()
            return event_id

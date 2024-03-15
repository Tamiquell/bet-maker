from dto.bets import AddBetDTO, BetDTO, GetFilterByEventID, UpdateBetDTO
from utils.unit_of_work import IUnitOfWork


class BetService:
    def __init__(self, uow: IUnitOfWork) -> None:
        self.uow = uow

    async def add_bet(self, bet_data: AddBetDTO):
        bet_dict = bet_data.model_dump()
        bet_dict["status"] = "in process"
        async with self.uow:
            bet_id = await self.uow.bets.add_one(bet_dict)
            await self.uow.commit()
            return bet_id

    async def get_bets(self, event_id: int | None):
        async with self.uow:
            all_bets = await self.uow.bets.find_all(event_id=event_id)
            return all_bets

    async def get_bet_by_id(self, bet_id: int):
        async with self.uow:
            one_bet = await self.uow.bets.find_one(id=bet_id)
            return one_bet

    async def update_bet(self, bet_ids: list[int], data: UpdateBetDTO):
        bet_dict = data.model_dump(exclude_none=True)
        async with self.uow:
            for bet_id in bet_ids:
                updated_bet = await self.uow.bets.edit_one(
                    id=bet_id, data=bet_dict)
            await self.uow.commit()
            return updated_bet

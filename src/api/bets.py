from fastapi import APIRouter, Depends

from api.dependencies import UOWDep
from dto.bets import AddBetDTO, BetDTO, GetFilterByEventID
from services.bets import BetService

bets_router = APIRouter(prefix="/bets", tags=["Bets"])


@bets_router.post("")
async def add_new_bet(data: AddBetDTO, uow: UOWDep):
    bet_id = await BetService(uow=uow).add_bet(data)
    return bet_id


@bets_router.get("")
async def get_all_bets(
        uow: UOWDep,
        filters: GetFilterByEventID = Depends(GetFilterByEventID),
) -> list[BetDTO]:
    all_bets = await BetService(uow=uow).get_bets(event_id=filters.event_id)
    return all_bets

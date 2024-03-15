from sqlalchemy import select

from db.models.bets import Bet
from db.repositories.base import SQLAlchemyRepository


class BetRepository(SQLAlchemyRepository):
    model = Bet

    async def find_all(self, **filter_by):
        stmt = select(self.model)
        if filter_by['event_id']:
            stmt = stmt.filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

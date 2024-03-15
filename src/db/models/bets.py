from sqlalchemy import Enum, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.utils.base import Base
from dto.bets import BetDTO


class Bet(Base):

    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[str] = mapped_column(Float(2))
    status: Mapped[str] = mapped_column(
        Enum("in process", "win", "lose", name="status"),
        nullable=False
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", ondelete="CASCADE"), nullable=False
    )

    def to_read_model(self) -> BetDTO:
        return BetDTO(
            id=self.id,
            amount=self.amount,
            status=self.status,
            event_id=self.event_id
        )

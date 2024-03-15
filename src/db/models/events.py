from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from db.utils.base import Base
from dto.events import EventDTO


class Event(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_1: Mapped[str] = mapped_column(nullable=False)
    team_2: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("in process", "win", "lose", name="status"),
        nullable=False
    )

    def to_read_model(self) -> EventDTO:
        return EventDTO(
            id=self.id,
            team_1=self.team_1,
            team_2=self.team_2,
            status=self.status
        )

from db.models.events import Event
from db.repositories.base import SQLAlchemyRepository


class EventRepository(SQLAlchemyRepository):
    model = Event

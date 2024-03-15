from pydantic import BaseModel, Field, condecimal


class AddBetDTO(BaseModel):
    event_id: int
    amount: float = condecimal(decimal_places=2)


class BetDTO(BaseModel):
    id: int
    amount: float = condecimal(decimal_places=2)
    status: str
    event_id: int


class UpdateBetDTO(BaseModel):
    status: str


class GetFilterByEventID(BaseModel):
    event_id: int | None = Field(default=None)

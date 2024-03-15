from typing import Literal

from pydantic import BaseModel


class UpdateEventDTO(BaseModel):
    status: Literal["win", "lose"]


class EventDTO(BaseModel):
    id: int
    team_1: str
    team_2: str
    status: str


class AddEventDTO(BaseModel):
    team_1: str
    team_2: str
    status: str

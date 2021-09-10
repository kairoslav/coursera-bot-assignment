from typing import NamedTuple


class User(NamedTuple):
    user_id: int


class Place(NamedTuple):
    place_id: int
    name: str
    longitude: float
    latitude: float

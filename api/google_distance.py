import asyncio
from typing import Optional, NamedTuple

import aiohttp
from pydantic import BaseModel

from data.config import GOOGLE_DISTANCE_MATRIX_API_KEY as API_KEY
from my_types import Place, User
from utils.db_api.db_methods import get_user_places


class Location(NamedTuple):
    place: Place
    distance: int


class TextValue(BaseModel):
    text: str
    value: int


class DistanceMatrixElement(BaseModel):
    distance: Optional[TextValue]
    duration: Optional[TextValue]
    status: str


class DistanceMatrixRow(BaseModel):
    elements: list[DistanceMatrixElement]


class GoogleApiResponse(BaseModel):
    destination_addresses: list[str]
    origin_addresses: list[str]
    rows: list[DistanceMatrixRow]
    status: str


async def get_nearest_locations(user: User, place: Place, radius=1500):
    """ Method for getting data from google Matrix Distance Api
        radius is the maximum range of nearest place in meters
    """
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    user_places = get_user_places(user.user_id)
    origins = f"{place.latitude},{place.longitude}"
    destinations = ""
    distances = []
    for _user_id, name, longitude, latitude in user_places:
        destinations += f"{latitude},{longitude}|"
    async with aiohttp.ClientSession() as session:
        params = {
            "origins": origins,
            "destinations": destinations,
            "key": API_KEY
        }
        async with session.get(url, params=params) as resp:
            response = await resp.text()
            api_model = GoogleApiResponse.parse_raw(response)
    for row in api_model.rows:
        for element in row.elements:
            if element.status == "OK":
                distances.append(element.distance.value)
            else:
                distances.append(None)
    nearest_locations = []

    for _place, distance in zip(user_places, distances):
        if distance is not None:
            if distance <= radius:
                nearest_locations.append(Location(Place(*_place), distance))

    return nearest_locations


if __name__ == '__main__':
    user = User(225828905)
    place = Place(
        place_id=0,
        name="test",
        longitude=30.424145,
        latitude=60.043369
    )
    print(asyncio.run(get_nearest_locations(user, place)))

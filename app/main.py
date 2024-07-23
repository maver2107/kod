from fastapi import FastAPI, Query, Depends
from datetime import date
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        number_of_people: int,
        has_SPA: bool = None,
        stars: int = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.number_of_people = number_of_people
        self.has_SPA = has_SPA
        self.stars = stars

class Shotel(BaseModel):
    adress: str
    name: str
    stars: int


@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
):
    return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
    all_inclusive: bool
    

@app.post("/boolings")
def add_booking(booking: SBooking):
    pass


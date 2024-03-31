from fastapi import FastAPI

from src.ste.inst import Experiement

app = FastAPI()
"""
This module contains the FastAPI application and the endpoints for the API.
"""


app = FastAPI()

"""
Create an instance of the Experiment class.
"""
exp = Experiement()


@app.get("/station")
async def get_station():
    """
    Endpoint to get the current state of the station.
    """
    ste = exp.show_station()
    return ste


@app.post("/create_instrument/{inst_name}")
async def add_parameter(inst_name: str):
    """
    Endpoint to create a new instrument and add it to the station.
    """
    exp.create_instrument(name=inst_name)
    ste = exp.show_station()
    return ste

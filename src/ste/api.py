from fastapi import FastAPI
from src.ste.inst import Experiement

app = FastAPI()


exp = Experiement()


@app.get("/station")
async def get_station():
    ste = exp.show_station()
    return ste


@app.post("/create_instrument/{inst_name}")
async def add_parameter(inst_name: str):
    exp.create_instrument(name=inst_name)
    ste = exp.show_station()
    return ste


# Run the application
# uvicorn main:app --reload

from qcodes.instrument_drivers.mock_instruments import DummyInstrument
from qcodes.utils import validators as vals
from qcodes.station import Station


class Experiement:
    def __init__(self) -> None:
        self.ste = Station()

    def create_instrument(self, name: str):
        _inst = DummyInstrument(name=name)
        self.ste.add_component(_inst, name)

    def show_station(self):
        return self.ste.snapshot()

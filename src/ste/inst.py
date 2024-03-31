"""
This module contains the Experiment class which is used to manage the instruments in the station.
"""

from qcodes.instrument_drivers.mock_instruments import DummyInstrument
from qcodes.station import Station
from qcodes.utils import validators as vals


class Experiement:
    """
    The Experiment class is used to create and manage instruments in a station.
    """

    def __init__(self) -> None:
        """
        Initialize the Experiment with a new Station.
        """
        self.ste = Station()

    def create_instrument(self, name: str):
        """
        Create a new DummyInstrument and add it to the station.

        Args:
            name (str): The name of the instrument.

        Returns:
            None
        """
        _inst = DummyInstrument(name=name)
        self.ste.add_component(_inst, name)

    def show_station(self):
        """
        Return a snapshot of the current state of the station.

        Returns:
            dict: A dictionary representing the current state of the station.
        """
        return self.ste.snapshot()

#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city object.

    Attributes:
        state_id (str): The ID of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

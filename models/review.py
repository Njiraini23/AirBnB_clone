#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class has public attributes
    """
    place_id = ""
    user_id = ""
    text = ""


def __init__(self, *args, **kwargs):
    """
    init
    """
    super().__init__(*args, **kwargs)

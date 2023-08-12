#!/usr/bin/python3
"""Module that defines review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""

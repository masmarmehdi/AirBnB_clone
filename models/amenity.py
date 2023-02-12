#!/usr/bin/python3
'''class Amenity that inherits from BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class to represent Amenity

        attributes:
            name (str): name of amenity
    '''

    name = ''

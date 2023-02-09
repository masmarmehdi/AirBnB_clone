#!/usr/bin/python3
'''class City that inherits from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''class to represent city
    
        attributes:
            name (str): name of city
            state_id (str): state id
    '''

    state_id = ''
    name = ''
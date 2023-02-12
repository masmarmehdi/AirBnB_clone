#!/usr/bin/python3
'''class State that inherits from BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class to represent state

        attributes:
            name (str): name of state
    '''

    name = ''

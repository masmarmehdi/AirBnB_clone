#!/usr/bin/python3
'''class Review that inherits from BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class to represent Review

        attributes:
            place_id (str): place id
            user_id (str): user id
            text (str): review text
    '''

    place_id = ''
    user_id = ''
    text = ''

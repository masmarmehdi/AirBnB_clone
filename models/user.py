#!/usr/bin/python3
'''User class that inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class to hold User information
    
    Attributes:
        email (str): email of user
        password (str): user password
        first_name (str): user first name
        last_name (str): user last name
    '''

    
    email = ''
    password = ''
    first_name = ''
    last_name = ''
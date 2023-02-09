#!/usr/bin/python3
'''class Place that inherits from BaseModel'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''class to represent Place
    
        attributes:
            city_id (str): city id
            user_id (str): user id
            name (str): name of state
            description (srt): description of place
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathrooms
            max_guest (int): maximum number of guests
            price_by_night (int): price of place by night
            latitude (float): latitude of place
            longitude (float): longitude of place
            amenity_ids (list of strings): amenity ids
    '''
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
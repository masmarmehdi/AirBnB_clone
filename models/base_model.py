#!/usr/bin/python3
'''BaseModel that defines all common attributes for other classes'''
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''Class to define attributes and classes'''

    def __init__(self, *args, **kwargs):
        '''
        Initialize new BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): key value pair of attribute
        '''
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        '''Update datetime'''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def __str__(self):
        '''Return string representation of object'''
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

#!/usr/bin/python3
'''FileStorage class that serialize instances to Json
and Deserialize Json file to instances
'''
import models

class FileStorage:
    '''class to serialize and deserialize instances
    
    Attributes:
        __file_path (str): name of file
        __objects (dict): A dictionary of object instance
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''return dictionary of __objects'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''set __objects in obj with key <obj class name>.id'''
        

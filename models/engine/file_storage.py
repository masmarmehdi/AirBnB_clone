#!/usr/bin/python3
'''FileStorage class that serialize instances to Json
and Deserialize Json file to instances
'''

import json

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
        oj_cls = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(oj_cls, obj.id)] = obj

    def save(self):
        '''Serializes __objects to JSON file path'''
        all_obj = FileStorage.__objects
        obj_dict = {}
        for object in all_obj.keys():
            obj_dict[object] = all_obj[object].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)
    
    def reload(self):
        '''Deserialize the JSON file in path to object if it exists'''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json.load(file)
        except FileNotFoundError:
            return

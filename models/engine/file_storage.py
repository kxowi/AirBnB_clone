#!/usr/bin/python3
"""
Module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


class FileStorage():
    """Serialize and deserialize of an instance"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """Append new obj to the dictionary __objects

            Args:
                obj(object) : the object to be added
        """
        if obj:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serialize __objects to JSON format"""
        with open(FileStorage.__file_path, "w", encoding='UTF-8') as f:
            save_obj = {}
            for k, v in self.__objects.items():
                save_obj[k] = v.to_dict()
            json.dump(save_obj, f)

    def reload(self):
        """Deserialize __objects fro JSON format"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='UTF-8') as f:
                storage_objs = json.load(f)
                for k, v in storage_objs.items():
                    self.__objects[k] = classes[v['__class__']](**v)
        else:
            FileStorage._FileStorage__objects = {}

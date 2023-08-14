#!/usr/bin/python3
"""Module that defines BaseModule class"""

import uuid as ud
from datetime import datetime


class BaseModel():
    """Defines commun attributes & methodes for all
    other subclasses"""

    def __init__(self, *args, **kwargs):
        """Constructor for the attributes"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.fromisoformat(v)
                elif k == '__class__':
                    pass
                else:
                    self.__setattr__(k, v)

        else:
            self.id = str(ud.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Override str method"""
        return ("[{}] ({}) ({})".format(
            self.__class__.__name__,
            self.id,
            self.__dict__))

    def save(self):
        """Save the instance"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of a __dict__ of the instance"""
        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = self.__class__.__name__
        return d

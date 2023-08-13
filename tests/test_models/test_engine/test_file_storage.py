#!/usr/bin/python3
"""Module that defines unittest for FileStorage class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import unittest
import json
import os


class TestFileStorage(unittest.TestCase):
    """Defines test cases for FileStorage class"""

    def test_docstring(self):
        """Check docstrings"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)
        self.assertTrue(len(FileStorage.all.__doc__) >= 1)
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)
        self.assertTrue(len(FileStorage.save.__doc__) >= 1)
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1)

    def test_attrs(self):
        """Check for attributes"""
        stg = FileStorage()
        attributes = [
                '_FileStorage__file_path',
                '_FileStorage__objects'
                ]
        for attr in attributes:
            self.assertTrue(hasattr(stg, attr))
        self.assertEqual(type(stg), FileStorage)
        self.assertEqual(
                type(FileStorage._FileStorage__file_path), str)

    def test_all(self):
        """Test cases for all method"""
        b = BaseModel()
        b.save()
        stg = FileStorage()
        self.assertIn(b, stg.all().values())
        self.assertEqual(type(stg.all()), dict)

        with self.assertRaises(TypeError):
            stg.all(None)

    def test_new(self):
        """Test cases for new method"""
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        p = Place()
        a = Amenity()
        r = Review()
        stg = FileStorage()

        self.assertIn(b, stg.all().values())
        self.assertIn(u, stg.all().values())
        self.assertIn(s, stg.all().values())
        self.assertIn(c, stg.all().values())
        self.assertIn(p, stg.all().values())
        self.assertIn(a, stg.all().values())
        self.assertIn(r, stg.all().values())
        with self.assertRaises(TypeError):
            stg.new()

    def test_save(self):
        """Test cases for save method"""
        b = BaseModel()
        b.save()
        stg = FileStorage()
        stg.save()
        path = FileStorage._FileStorage__file_path
        with open(path, "r", encoding="UTF-8") as f:
            data = json.load(f)
            key = 'BaseModel.' + b.id
            self.assertIn(key, data.keys())
        with self.assertRaises(TypeError):
            stg.save(None)
        u = User()
        s = State()
        c = City()
        p = Place()
        a = Amenity()
        r = Review()
        stg.save()

        objs = stg.all()
        with open(path, "r", encoding="UTF-8") as f:
            data = json.load(f)

            self.assertIn('BaseModel.' + b.id, objs)
            self.assertIn('User.' + u.id, objs)
            self.assertIn('State.' + s.id, objs)
            self.assertIn('City.' + c.id, objs)
            self.assertIn('Place.' + p.id, objs)
            self.assertIn('Amenity.' + a.id, objs)
            self.assertIn('Review.' + r.id, objs)

    def test_reload(self):
        """Test cases for reload method"""
        b = BaseModel()
        u = User()
        s = State()
        c = City()
        p = Place()
        a = Amenity()
        r = Review()

        stg = FileStorage()
        path = FileStorage._FileStorage__file_path
        stg.save()
        stg.reload()
        objs = stg.all()

        with open(path, "r", encoding="UTF-8") as f:
            data = json.load(f)

            self.assertIn('BaseModel.' + b.id, objs)
            self.assertIn('User.' + u.id, objs)
            self.assertIn('State.' + s.id, objs)
            self.assertIn('City.' + c.id, objs)
            self.assertIn('Place.' + p.id, objs)
            self.assertIn('Amenity.' + a.id, objs)
            self.assertIn('Review.' + r.id, objs)


if __name__ == "__main__":
    unittest.main()

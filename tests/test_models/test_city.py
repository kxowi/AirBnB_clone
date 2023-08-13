#!/usr/bin/python3
"""Module that defines unittest for City class"""

from models.city import City
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestCity(unittest.TestCase):
    """Desfines testcases for City class"""

    def test_attributes(self):
        """Test cases for City attributes"""
        c = City()
        attributes = [
                'id',
                'created_at',
                'updated_at',
                'state_id',
                'name',
                ]
        for attr in attributes:
            self.assertTrue(hasattr(c, attr))

    def test_str(self):
        """Test cases for str method"""
        c = City()
        expected_string = f"[City] ({c.id}) ({c.__dict__})"
        self.assertEqual(expected_string, str(c))

    def test_to_dict(self):
        """Test cases for to_dict method"""
        c = City()
        c.name = "honcong"
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'name',
                '__class__'
                ]
        self.assertEqual(expected_result, list(c.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        c = City()
        c.created_at = c.updated_at = dt.datetime.now()
        self.assertEqual(c.created_at, c.updated_at)
        c.save()
        self.assertNotEqual(c.created_at, c.updated_at)
        key = 'City.' + c.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())

    def test_instance(self):
        """Is subclass and instance of User class"""
        c = City()
        self.assertIsInstance(c, City)
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()

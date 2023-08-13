#!/usr/bin/python3
"""Module that defines unittest for Amenity class"""

from models.amenity import Amenity
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestAmenity(unittest.TestCase):
    """Desfines testcases for Amenity class"""

    def test_creation(self):
        """Test creation of Amenity instances"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1, a2)
        for attr in ['id', 'created_at', 'updated_at', 'name']:
            self.assertTrue(hasattr(a1, attr) and hasattr(a2, attr))

    def test_attrs_type(self):
        """Check type of attrs and value"""
        a = Amenity()
        self.assertEqual(type(a.name), str)
        self.assertEqual(a.name, "")

    def test_str(self):
        """Test cases for str method"""
        a = Amenity()
        expected_string = f"[Amenity] ({a.id}) ({a.__dict__})"
        self.assertEqual(expected_string, str(a))

    def test_to_dict(self):
        """Test cases for to_dict method"""
        a = Amenity()
        a.name = "amenity"
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'name',
                '__class__'
                ]
        self.assertEqual(expected_result, list(a.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        a = Amenity()
        a.created_at = a.updated_at = dt.datetime.now()
        self.assertEqual(a.created_at, a.updated_at)
        a.save()
        self.assertNotEqual(a.created_at, a.updated_at)
        key = 'Amenity.' + a.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())

    def test_instance(self):
        """Is subclass and instance of User class"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()

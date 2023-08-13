#!/usr/bin/python3
"""Module that defines unittest for Place class"""

from models.place import Place
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestPlace(unittest.TestCase):
    """Desfines testcases for Place class"""

    def test_creation(self):
        """Create an instance of Place class"""
        p = Place()
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(Place, BaseModel))
        attributes = [
                'id',
                'created_at',
                'updated_at',
                'city_id',
                'user_id',
                'name',
                'description',
                'number_rooms',
                'number_bathrooms',
                'max_guest',
                'price_by_night',
                'latitude',
                'longitude',
                'amenity_ids',
                ]
        for attr in attributes:
            self.assertTrue(hasattr(p, attr))

    def test_attrs_type(self):
        """Check type of attrs and value"""
        p = Place()
        self.assertEqual(type(p.city_id), str)
        self.assertEqual(type(p.user_id), str)
        self.assertEqual(type(p.name), str)
        self.assertEqual(type(p.description), str)
        self.assertEqual(type(p.number_rooms), int)
        self.assertEqual(type(p.number_bathrooms), int)
        self.assertEqual(type(p.max_guest), int)
        self.assertEqual(type(p.price_by_night), int)
        self.assertEqual(type(p.latitude), float)
        self.assertEqual(type(p.longitude), float)
        self.assertEqual(type(p.amenity_ids), list)

        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])

    def test_to_dict(self):
        """Test cases for to_dict method"""
        p = Place()
        p.name = "halimon"
        p.description = "great place"
        p.number_rooms = 10
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'name',
                'description',
                'number_rooms',
                '__class__'
                ]
        self.assertEqual(expected_result, list(p.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        p = Place()
        p.created_at = p.updated_at = dt.datetime.now()
        self.assertEqual(p.created_at, p.updated_at)
        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)
        key = 'Place.' + p.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())


if __name__ == "__main__":
    unittest.main()

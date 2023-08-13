#!/usr/bin/python3
"""Module that defines unittest for State class"""

from models.state import State
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestState(unittest.TestCase):
    """Desfines testcases for State class"""

    def test_creation(self):
        """Test creation of State instances"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1, s2)
        for attr in ['id', 'created_at', 'updated_at', 'name']:
            self.assertTrue(hasattr(s1, attr))

    def test_str(self):
        """Test cases for str method"""
        s = State()
        expected_string = f"[State] ({s.id}) ({s.__dict__})"
        self.assertEqual(expected_string, str(s))

    def test_to_dict(self):
        """Test cases for to_dict method"""
        s = State()
        s.name = "state"
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'name',
                '__class__'
                ]
        self.assertEqual(expected_result, list(s.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        s = State()
        s.created_at = s.updated_at = dt.datetime.now()
        self.assertEqual(s.created_at, s.updated_at)
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)
        key = 'State.' + s.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())

    def test_instance(self):
        """Is subclass and instance of User class"""
        s = State()
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()

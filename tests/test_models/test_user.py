#!/usr/bin/python3
"""Module that defines unittest for User class"""

from models.user import User
from models.base_model import BaseModel
import models
import unittest


class TestUser(unittest.TestCase):
    """Desfines testcases for User class"""

    def test_attributes(self):
        """Test cases for User attributes"""
        u = User()
        attributes = [
                'id',
                'created_at',
                'updated_at',
                'email',
                'password',
                'first_name',
                'last_name'
                ]
        for attr in attributes:
            self.assertTrue(hasattr(u, attr))

        self.assertTrue(type(u.first_name), str)
        self.assertTrue(type(u.last_name), str)
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertTrue(issubclass(type(u), BaseModel))
        self.assertIsInstance(u, User)

    def test_str(self):
        """Test cases for str method"""
        u = User()
        expected_string = f"[User] ({u.id}) ({u.__dict__})"
        self.assertEqual(expected_string, str(u))

    def test_to_dict(self):
        """Test cases for to_dict method"""
        u = User()
        u.email = "e@email"
        u.password = "root"
        u.first_name = "nicol"
        u.last_name = "nermax"
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'email',
                'password',
                'first_name',
                'last_name',
                '__class__'
                ]
        self.assertEqual(expected_result, list(u.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        u = User()
        u.save()
        key = 'User.' + u.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())

    def test_instance(self):
        """Is subclass and instance of User class"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()

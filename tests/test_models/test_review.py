#!/usr/bin/python3
"""Module that defines unittest for Review class"""

from models.review import Review
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestReview(unittest.TestCase):
    """Desfines testcases for Review class"""

    def test_creation(self):
        """Create an instance of Review class"""
        r = Review()
        r.text = "good place ever"
        self.assertEqual(r.text, "good place ever")
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_str(self):
        """Test cases for str method"""
        r = Review()
        self.assertIn(r, models.storage.all().values())

    def test_to_dict(self):
        """Test cases for to_dict method"""
        r = Review()
        r.text = "good place ever"
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'text',
                '__class__'
                ]
        self.assertEqual(expected_result, list(r.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        r = Review()
        r.save()
        key = 'Review.' + r.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())


if __name__ == "__main__":
    unittest.main()

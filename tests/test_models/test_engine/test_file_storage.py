#!/usr/bin/python3
"""Module that defines unittest for FileStorage class"""

from models.engine.file_storage import FileStorage
from models.user import User
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

    def test_all(self):
        """Test cases for all method"""
        u = User()
        u.save()
        stg = FileStorage()
        self.assertIn(u, stg.all().values())
        self.assertEqual(type(stg.all()), dict)

    def test_new(self):
        """Test cases for new method"""
        u = User()
        u.save()
        stg = FileStorage()
        stg.new(u)
        self.assertIn(u, stg.all().values())
        with self.assertRaises(TypeError):
            stg.new()

    def test_save(self):
        """Test cases for save method"""
        u = User()
        u.save
        stg = FileStorage()
        stg.save()
        with open("file.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            key = 'User.' + u.id
            self.assertIn(key, data.keys())

    def test_reload(self):
        """Test cases for reload method"""
        u = User()
        u.save()
        stg = FileStorage()
        key = 'User.' + u.id
        stg.reload()
        self.assertIn(key, stg.all().keys())
        FileStorage.__file_path = ""
        self.assertFalse(os.path.exists(FileStorage.__file_path))


if __name__ == "__main__":
    unittest.main()

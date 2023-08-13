#!/usr/bin/python3
"""Module that defines unittest for FileStorage class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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
        b = BaseModel()
        b.save()
        stg = FileStorage()
        self.assertIn(b, stg.all().values())
        self.assertEqual(type(stg.all()), dict)

    def test_new(self):
        """Test cases for new method"""
        b = BaseModel()
        b.save()
        stg = FileStorage()
        stg.new(b)
        self.assertIn(b, stg.all().values())
        with self.assertRaises(TypeError):
            stg.new()

    def test_save(self):
        """Test cases for save method"""
        b = BaseModel()
        b.save()
        stg = FileStorage()
        stg.save()
        with open("file.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            key = 'BaseModel.' + b.id
            self.assertIn(key, data.keys())

    def test_reload(self):
        """Test cases for reload method"""
        b = BaseModel()
        b.save()
        stg = FileStorage()
        key = 'BaseModel.' + b.id
        stg.reload()
        self.assertIn(key, stg.all().keys())
        FileStorage.__file_path = ""
        self.assertFalse(os.path.exists(FileStorage.__file_path))

    def test_file_not_found(self):
        """Case if the file not found"""
        stg = FileStorage()
        stg.__file_path = "no exesting path"
        with self.assertRaises(FileNotFoundError):
            with open(stg.__file_path, "r", encoding="UTF-8") as f:
                pass


if __name__ == "__main__":
    unittest.main()

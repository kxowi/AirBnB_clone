#!/usr/bin/python3
"""Module that defines unittest for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """BaseModel unittests"""

    def test_docstring(self):
        """Check docstrings"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)

    def test_attrs(self):
        """Test cases for BaseModel attributes"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)
        attributes = [
                'id',
                'created_at',
                'updated_at'
                ]
        for attr in attributes:
            self.assertTrue(hasattr(b1, attr))

    def test_str(self):
        """Test cases for str method"""
        base = BaseModel()
        result = base.__str__()

        ex_result = f"[BaseModel] ({base.id}) ({base.__dict__})"
        self.assertEqual(result, ex_result)

    def test_save(self):
        """Test cases for save method"""
        base = BaseModel()
        created1 = base.created_at
        updated1 = base.updated_at
        base.save()
        created2 = base.created_at
        updated2 = base.updated_at
        self.assertEqual(created1, created2)
        self.assertNotEqual(updated1, updated2)

    def test_to_dict(self):
        """Test cases for to-dict method"""
        base = BaseModel()
        dic = base.to_dict()
        keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertEqual(keys, list(dic.keys()))


if __name__ == "__main__":
    unittest.main()

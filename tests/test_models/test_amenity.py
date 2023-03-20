#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
"""
import unittest
import uuid
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Create object of Amenity class for testing.
    """
    def setUp(self):
        self.test1 = Amenity()
        self.test2 = Amenity()

    """
    Test object attributes.
    """
    def test_attribute(self):
        self.assertTrue(hasattr(self.test1, "name"))
        self.assertFalse(hasattr(self.test2, "place"))
        self.assertTrue(type(self.test1.name) is str)
        self.assertTrue(type(self.test2.id) is str)
        self.assertTrue(self.test1.id != self.test2.id)
        test_created1 = self.test1.created_at
        test_created2 = self.test2.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

    """
    Test inherited methods.
    """
    def test_save(self):
        test_updated = self.test1.updated_at
        self.test1.save()
        updated_save = self.test1.updated_at
        self.assertFalse(test_updated == updated_save)

    """
    Test dynamic method creation
    """
    def test_count(self):
        self.assertFalse(hasattr(self.test1, "do_count()"))

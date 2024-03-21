#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_initialization(self):
        """Test initialization of Amenity."""
        # Verify if an Amenity instance is created successfully
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

        # Test if default value for attribute is correctly set
        self.assertEqual(amenity.name, "")

        # Verify that Amenity instances have unique ids
        amenity_2 = Amenity()
        self.assertNotEqual(amenity.id, amenity_2.id)

    def test_attribute_assignment(self):
        """Test attribute assignment of Amenity."""
        amenity = Amenity(
            name="Swimming Pool"
        )
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_attribute_types(self):
        """Test attribute types of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_edge_cases(self):
        """Test edge cases for attribute assignment."""
        # Test assigning empty string to attribute
        amenity = Amenity(
            name=""
        )
        self.assertEqual(amenity.name, "")

        # Test assigning None value to attribute
        amenity = Amenity(
            name=None
        )
        self.assertIsNone(amenity.name)

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple Amenity instances."""
        # Verify that Amenity instances have unique ids
        amenity_1 = Amenity()
        amenity_2 = Amenity()
        self.assertNotEqual(amenity_1.id, amenity_2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        amenity = Amenity(
            name="Gym"
        )
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Gym")

        # Test deserialization
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.name, "Gym")

    def test_str_representation(self):
        """Test the string representation of Amenity."""
        amenity = Amenity(
            name="Pool"
        )
        self.assertIn("Amenity", str(amenity))
        self.assertIn(amenity.name, str(amenity))

if __name__ == "__main__":
    unittest.main()

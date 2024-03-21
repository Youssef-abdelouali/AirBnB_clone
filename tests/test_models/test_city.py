#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_initialization(self):
        """Test initialization of City."""
        # Verify if a City instance is created successfully
        city = City()
        self.assertIsInstance(city, City)

        # Test if default values for attributes are correctly set
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        # Verify that City instances have unique ids
        city_2 = City()
        self.assertNotEqual(city.id, city_2.id)

    def test_attribute_assignment(self):
        """Test attribute assignment of City."""
        # Test if state_id and name attributes are properly assigned
        city = City(state_id="1", name="New York")
        self.assertEqual(city.state_id, "1")
        self.assertEqual(city.name, "New York")

    def test_edge_cases(self):
        """Test edge cases for attribute assignment."""
        # Test assigning empty strings to attributes
        city = City(state_id="", name="")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        # Test assigning None values to attributes
        city = City(state_id=None, name=None)
        self.assertIsNone(city.state_id)
        self.assertIsNone(city.name)

        # Test assigning invalid types to attributes
        with self.assertRaises(TypeError):
            city = City(state_id=123, name=True)

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple City instances."""
        # Verify that City instances have unique ids
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        city = City(state_id="1", name="New York")
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], "1")
        self.assertEqual(city_dict['name'], "New York")

        # Test deserialization
        new_city = City(**city_dict)
        self.assertEqual(new_city.state_id, "1")
        self.assertEqual(new_city.name, "New York")

if __name__ == "__main__":
    unittest.main()

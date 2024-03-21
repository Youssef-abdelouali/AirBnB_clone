#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_initialization(self):
        """Test initialization of Place."""
        # Verify if a Place instance is created successfully
        place = Place()
        self.assertIsInstance(place, Place)

        # Test if default values for attributes are correctly set
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        # Verify that Place instances have unique ids
        place_2 = Place()
        self.assertNotEqual(place.id, place_2.id)

    def test_attribute_assignment(self):
        """Test attribute assignment of Place."""
        # Test if attributes are properly assigned
        place = Place(
            city_id="1",
            user_id="2",
            name="Sample Place",
            description="A sample place for testing",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=123.456,
            longitude=789.012,
            amenity_ids=[1, 2, 3]
        )
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Sample Place")
        self.assertEqual(place.description, "A sample place for testing")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 123.456)
        self.assertEqual(place.longitude, 789.012)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_edge_cases(self):
        """Test edge cases for attribute assignment."""
        # Test assigning empty strings to attributes
        place = Place(
            city_id="",
            user_id="",
            name="",
            description="",
            number_rooms=0,
            number_bathrooms=0,
            max_guest=0,
            price_by_night=0,
            latitude=0.0,
            longitude=0.0,
            amenity_ids=[]
        )
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        # Test assigning None values to attributes
        place = Place(
            city_id=None,
            user_id=None,
            name=None,
            description=None,
            number_rooms=None,
            number_bathrooms=None,
            max_guest=None,
            price_by_night=None,
            latitude=None,
            longitude=None,
            amenity_ids=None
        )
        self.assertIsNone(place.city_id)
        self.assertIsNone(place.user_id)
        self.assertIsNone(place.name)
        self.assertIsNone(place.description)
        self.assertIsNone(place.number_rooms)
        self.assertIsNone(place.number_bathrooms)
        self.assertIsNone(place.max_guest)
        self.assertIsNone(place.price_by_night)
        self.assertIsNone(place.latitude)
        self.assertIsNone(place.longitude)
        self.assertIsNone(place.amenity_ids)

        # Test assigning invalid types to attributes
        with self.assertRaises(TypeError):
            place = Place(
                city_id=123,
                user_id=True,
                name=123,
                description=True,
                number_rooms="two",
                number_bathrooms="one",
                max_guest="four",
                price_by_night="one hundred",
                latitude="invalid",
                longitude="invalid",
                amenity_ids="invalid"
            )

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple Place instances."""
        # Verify that Place instances have unique ids
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        place = Place(
            city_id="1",
            user_id="2",
            name="Sample Place",
            description="A sample place for testing",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=123.456,
            longitude=789.012,
            amenity_ids=[1, 2, 3]
        )
        place_dict = place.to_dict()
        self.assertEqual(place_dict['city_id'], "1")
        self.assertEqual(place_dict['user_id'], "2")
        self.assertEqual(place_dict['name'], "Sample Place")
        self.assertEqual(place_dict['description'], "A sample place for testing")
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 123.456)
        self.assertEqual(place_dict['longitude'], 789.012)
        self.assertEqual(place_dict['amenity_ids'], [1, 2, 3])

        # Test deserialization
        new_place = Place(**place_dict)
        self.assertEqual(new_place.city_id, "1")
        self.assertEqual(new_place.user_id, "2")
        self.assertEqual(new_place.name, "Sample Place")
        self.assertEqual(new_place.description, "A sample place for testing")
        self.assertEqual(new_place.number_rooms, 2)
        self.assertEqual(new_place.number_bathrooms, 1)
        self.assertEqual(new_place.max_guest, 4)
        self.assertEqual(new_place.price_by_night, 100)
        self.assertEqual(new_place.latitude, 123.456)
        self.assertEqual(new_place.longitude, 789.012)
        self.assertEqual(new_place.amenity_ids, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()

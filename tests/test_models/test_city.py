#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    Test_City_instance_creation
    Test_City_save
    Test_City_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class Test_City_instance_creation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_with_no_args(self):
        self.assertEqual(City, type(City()))

    def test_with_new_instance_stored_in_objt(self):
        self.assertIn(City(), models.storage.all().values())

    def test_with_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))
    
    def test_for_updated_at_is_public(self):
        self.assertEqual(datetime, type(City().updated_at))
    
    def test_for_state_id_is_public(self):
        my_city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(my_city))
        self.assertNotIn("state_id", my_city.__dict__)

    def test_for_name_is_public_cls_attr(self):
        my_city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(my_city))
        self.assertNotIn("name", my_city.__dict__)

    def test_cities_with_unique_ids(self):
        my_city1 = City()
        my_city2 = City()
        self.assertNotEqual(my_city1.id, my_city2.id)

    def test_cities_with_different_created_at(self):
        my_city1 = City()
        sleep(0.05)
        my_city12 = City()
        self.assertLess(my_city1.created_at, my_city12.created_at)

    def test_double_cities_with_divers_updated_at(self):
        my_city1 = City()
        sleep(0.05)
        my_city2 = City()
        self.assertLess(my_city1.updated_at, my_city2.updated_at)

    def test_string_repres(self):
        date_time = datetime.today()
        date_repr = repr(date_time)
        my_city = City()
        my_city.id = "123456"
        my_city.created_at = my_city.updated_at = date_time
        my_city_ystr = my_city.__str__()
        self.assertIn("[City] (123456)", my_city_ystr)
        self.assertIn("'id': '123456'", my_city_ystr)
        self.assertIn("'created_at': " + date_repr, my_city_ystr)
        self.assertIn("'updated_at': " + date_repr, my_city_ystr)

    def test_unused_arguments(self):
        my_city = City(None)
        self.assertNotIn(None, my_city.__dict__.values())

    def test_for_instan_with_kwargs(self):
        date_time = datetime.today()
        date_format = date_time.isoformat()
        my_city = City(id="345", created_at=date_format, updated_at=date_format)
        self.assertEqual(my_city.id, "345")
        self.assertEqual(my_city.created_at, date_time)
        self.assertEqual(my_city.updated_at, date_time)

    def test_instantiation_without_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class Test_City_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        my_city= City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        self.assertLess(first_updated_at, my_city.updated_at)

    def test_for_two_saves(self):
        my_city= City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        my_city.save()
        second_updated_at = my_city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_city.save()
        self.assertLess(second_updated_at, my_city.updated_at)

    def test_for_save_with_arg(self):
        my_city= City()
        with self.assertRaises(TypeError):
            my_city.save(None)

    def test_for_save_updates_file(self):
        my_city= City()
        my_city.save()
        my_cityid = "City." + my_city.id
        with open("file.json", "r") as file:
            self.assertIn(my_cityid, file.read())


class Test_City_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_for_to_dict_includes_keys(self):
        my_city= City()
        self.assertIn("id", my_city.to_dict())
        self.assertIn("created_at", my_city.to_dict())
        self.assertIn("updated_at", my_city.to_dict())
        self.assertIn("__class__", my_city.to_dict())

    def test_for_to_dict_includes_added_attributes(self):
        my_city= City()
        my_city.middle_name = "Holberton"
        my_city.my_number = 98
        self.assertEqual("Holberton", my_city.middle_name)
        self.assertIn("my_number", my_city.to_dict())

    def test_for_to_dict_datetime_attr(self):
        my_city= City()
        my_city_dict = my_city.to_dict()
        self.assertEqual(str, type(my_city_dict["id"]))
        self.assertEqual(str, type(my_city_dict["created_at"]))
        self.assertEqual(str, type(my_city_dict["updated_at"]))

    def test_for_to_dict_output(self):
        date_time = datetime.today()
        my_city= City()
        my_city.id = "123456"
        my_city.created_at = my_city.updated_at = date_time
        time_dicti = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(my_city.to_dict(), time_dicti)

    def test_for_comparison_to_dict_and_dunder_dict(self):
        my_city= City()
        self.assertNotEqual(my_city.to_dict(), my_city.__dict__)

    def test_for_to_dict_with_arguments(self):
        my_city= City()
        with self.assertRaises(TypeError):
            my_city.to_dict(None)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class Test_Place_inst(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_for_no_args_inst(self):
        self.assertEqual(Place, type(Place()))

    def test_for_new_instance_stored_in_obj(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_for_id_is_public_string(self):
        self.assertEqual(str, type(Place().id))

    def test_for_created_at_is_public_date_time(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_for_updated_at_is_public_date_time(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_for_city_id_is_public_class_attr(self):
        my_Palce = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(my_Palce))
        self.assertNotIn("city_id", my_Palce.__dict__)

    def test_user_id_is_public_class_attribute(self):
        my_Palce = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(my_Palce))
        self.assertNotIn("user_id", my_Palce.__dict__)

    def test_for_name_is_public_class_attr(self):
        my_Palce = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(my_Palce))
        self.assertNotIn("name", my_Palce.__dict__)

    def test_for_descr_is_public_class_attr(self):
        my_Palce = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(my_Palce))
        self.assertNotIn("desctiption", my_Palce.__dict__)

    def test_for_number_rooms_is_public_class_attri(self):
        my_Palce = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(my_Palce))
        self.assertNotIn("number_rooms", my_Palce.__dict__)

    def test_for_num_bathrooms_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(my_Palce))
        self.assertNotIn("number_bathrooms", my_Palce.__dict__)

    def test_for_max_guest_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(my_Palce))
        self.assertNotIn("max_guest", my_Palce.__dict__)

    def test_for_price_by_night_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(my_Palce))
        self.assertNotIn("price_by_night", my_Palce.__dict__)

    def test_for_latitude_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(my_Palce))
        self.assertNotIn("latitude", my_Palce.__dict__)

    def test_for_longitude_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(my_Palce))
        self.assertNotIn("longitude", my_Palce.__dict__)

    def test_for_amenity_ids_is_public_cls_attr(self):
        my_Palce = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(my_Palce))
        self.assertNotIn("amenity_ids", my_Palce.__dict__)

    def test_for_two_places_with_unique_ids(self):
        my_place_1 = Place()
        my_place_2 = Place()
        self.assertNotEqual(my_place_1.id, my_place_2.id)

    def test_for_two_places_with_different_created_at(self):
        my_place_1 = Place()
        sleep(0.05)
        my_place_2 = Place()
        self.assertLess(my_place_1.created_at, my_place_2.created_at)

    def test_two_places_different_updated_at(self):
        my_place_1 = Place()
        sleep(0.05)
        my_place_2 = Place()
        self.assertLess(my_place_1.updated_at, my_place_2.updated_at)

    def test_for_string_repres(self):
        date_time = datetime.today()
        date_time_repre = repr(date_time)
        my_Palce = Place()
        my_Palce.id = "123456"
        my_Palce.created_at = my_Palce.updated_at = date_time
        Place_string = my_Palce.__str__()
        self.assertIn("[Place] (123456)", Place_string)
        self.assertIn("'id': '123456'", Place_string)
        self.assertIn("'created_at': " + date_time_repre, Place_string)
        self.assertIn("'updated_at': " + date_time_repre, Place_string)

    def test_for_unused_arguments(self):
        my_Palce = Place(None)
        self.assertNotIn(None, my_Palce.__dict__.values())

    def test_for_inst_with_kwargs(self):
        date_time = datetime.today()
        date_time_format = date_time.isoformat()
        my_Palce = Place(id="345", created_at=date_time_format, updated_at=date_time_format)
        self.assertEqual(my_Palce.id, "345")
        self.assertEqual(my_Palce.created_at, date_time)
        self.assertEqual(my_Palce.updated_at, date_time)

    def test_for_inst_without_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

class Test_Place_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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

    def test_for_one_save(self):
        my_Palce = Place()
        sleep(0.05)
        first_updated_at = my_Palce.updated_at
        my_Palce.save()
        self.assertLess(first_updated_at, my_Palce.updated_at)

    def test_for_double_saves(self):
        my_Palce = Place()
        sleep(0.05)
        first_updated_at = my_Palce.updated_at
        my_Palce.save()
        second_updated_at = my_Palce.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_Palce.save()
        self.assertLess(second_updated_at, my_Palce.updated_at)

    def test_for_save_with_arguments(self):
        my_Palce = Place()
        with self.assertRaises(TypeError):
            my_Palce.save(None)

    def test_for_save_updates_file(self):
        my_Palce = Place()
        my_Palce.save()
        Place_id = "Place." + my_Palce.id
        with open("file.json", "r") as file:
            self.assertIn(Place_id, file.read())

class Test_Place_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""
    def test_to_dict_(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_for_to_dict_with_correct_keys(self):
        my_Palce = Place()
        self.assertIn("id", my_Palce.to_dict())
        self.assertIn("created_at", my_Palce.to_dict())
        self.assertIn("updated_at", my_Palce.to_dict())
        self.assertIn("__class__", my_Palce.to_dict())

    def test_for_to_dict_with_added_attrs(self):
        my_Palce = Place()
        my_Palce.middle_name = "Holberton"
        my_Palce.my_number = 98
        self.assertEqual("Holberton", my_Palce.middle_name)
        self.assertIn("my_number", my_Palce.to_dict())

    def test_for_to_dict_date_time_attrs_are_strings(self):
        my_Palce = Place()
        Place_dict = my_Palce.to_dict()
        self.assertEqual(str, type(Place_dict["id"]))
        self.assertEqual(str, type(Place_dict["created_at"]))
        self.assertEqual(str, type(Place_dict["updated_at"]))

    def test_for_to_dict_outPut(self):
        date_time = datetime.today()
        my_Palce = Place()
        my_Palce.id = "123456"
        my_Palce.created_at = my_Palce.updated_at = date_time
        Time_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(my_Palce.to_dict(), Time_dict)

    def test_for_contrast_to_dict_dunder_dict(self):
        my_Palce = Place()
        self.assertNotEqual(my_Palce.to_dict(), my_Palce.__dict__)

    def test_to_dict_with_arg(self):
        my_Palce = Place()
        with self.assertRaises(TypeError):
            my_Palce.to_dict(None)

if __name__ == "__main__":
    unittest.main()

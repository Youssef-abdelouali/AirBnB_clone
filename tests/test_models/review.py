#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    Test_Review_instantiation
    Test_Review_save
    Test_Review_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class Test_Review_inst(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_without_args_inst(self):
        self.assertEqual(Review, type(Review()))

    def test_for_new_instance_stored_in_objt(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_for_id_is_public_string(self):
        self.assertEqual(str, type(Review().id))

    def test_for_created_at_is_public_date_time(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_for_updated_at_is_public_date_time(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_for_place_id_is_public_cls_attr(self):
        Revi_ew = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Revi_ew))
        self.assertNotIn("place_id", Revi_ew.__dict__)

    def test_for_user_id_is_public_class_attrs(self):
        Revi_ew = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Revi_ew))
        self.assertNotIn("user_id", Revi_ew.__dict__)

    def test_text_is_public_class_attribute(self):
        Revi_ew = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(Revi_ew))
        self.assertNotIn("text", Revi_ew.__dict__)

    def test_for_two_reviews_with_unique_id(self):
        Revi_ew_1 = Review()
        Revi_ew_2 = Review()
        self.assertNotEqual(Revi_ew_1.id, Revi_ew_2.id)

    def test_two_reviews_different_created_at(self):
        Revi_ew_1 = Review()
        sleep(0.05)
        Revi_ew_2 = Review()
        self.assertLess(Revi_ew_1.created_at, Revi_ew_2.created_at)

    def test_for_double_reviews_different_updated_at(self):
        Revi_ew_1 = Review()
        sleep(0.05)
        Revi_ew_2 = Review()
        self.assertLess(Revi_ew_1.updated_at, Revi_ew_2.updated_at)

    def test_for_string_repres(self):
        date_time = datetime.today()
        date_repres = repr(date_time)
        Revi_ew = Review()
        Revi_ew.id = "123456"
        Revi_ew.created_at = Revi_ew.updated_at = date_time
        Review_string = Revi_ew.__str__()
        self.assertIn("[Review] (123456)", Review_string)
        self.assertIn("'id': '123456'", Review_string)
        self.assertIn("'created_at': " + date_repres, Review_string)
        self.assertIn("'updated_at': " + date_repres, Review_string)

    def test_for_unused_args(self):
        Revi_ew = Review(None)
        self.assertNotIn(None, Revi_ew.__dict__.values())

    def test_for_inst_with_kwargs(self):
        date_time = datetime.today()
        date_isoFormat = date_time.isoformat()
        Revi_ew = Review(id="345", created_at=date_isoFormat, updated_at=date_isoFormat)
        self.assertEqual(Revi_ew.id, "345")
        self.assertEqual(Revi_ew.created_at, date_time)
        self.assertEqual(Revi_ew.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

class Test_Review_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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
        Revi_ew = Review()
        sleep(0.05)
        first_updated_at = Revi_ew.updated_at
        Revi_ew.save()
        self.assertLess(first_updated_at, Revi_ew.updated_at)

    def test_for_two_saves(self):
        Revi_ew = Review()
        sleep(0.05)
        first_updated_at = Revi_ew.updated_at
        Revi_ew.save()
        second_updated_at = Revi_ew.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Revi_ew.save()
        self.assertLess(second_updated_at, Revi_ew.updated_at)

    def test_for_save_with_arguments(self):
        Revi_ew = Review()
        with self.assertRaises(TypeError):
            Revi_ew.save(None)

    def test_for_save_updates_file(self):
        Revi_ew = Review()
        Revi_ew.save()
        Review_id = "Review." + Revi_ew.id
        with open("file.json", "r") as file:
            self.assertIn(Review_id, file.read())

class Test_Review_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_for_to_dict_includes_correct_keys(self):
        Revi_ew = Review()
        self.assertIn("id", Revi_ew.to_dict())
        self.assertIn("created_at", Revi_ew.to_dict())
        self.assertIn("updated_at", Revi_ew.to_dict())
        self.assertIn("__class__", Revi_ew.to_dict())

    def test_for_to_dict_includes_added_attr(self):
        Revi_ew = Review()
        Revi_ew.middle_name = "Holberton"
        Revi_ew.my_number = 98
        self.assertEqual("Holberton", Revi_ew.middle_name)
        self.assertIn("my_number", Revi_ew.to_dict())

    def test_to_dict_date_time_attr_are_strings(self):
        Revi_ew = Review()
        Review_dict = Revi_ew.to_dict()
        self.assertEqual(str, type(Review_dict["id"]))
        self.assertEqual(str, type(Review_dict["created_at"]))
        self.assertEqual(str, type(Review_dict["updated_at"]))

    def test_for_to_dict_opt(self):
        date_time = datetime.today()
        Revi_ew = Review()
        Revi_ew.id = "123456"
        Revi_ew.created_at = Revi_ew.updated_at = date_time
        time_dict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(Revi_ew.to_dict(), time_dict)

    def test_for_comparison_to_dict_dunder_dict(self):
        Revi_ew = Review()
        self.assertNotEqual(Revi_ew.to_dict(), Revi_ew.__dict__)

    def test_for_to_dict_with_arguments(self):
        Revi_ew = Review()
        with self.assertRaises(TypeError):
            Revi_ew.to_dict(None)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class Test8User_inst(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_for_instantiates_without_arguments(self):
        self.assertEqual(User, type(User()))

    def test_for_new_instance_stored_in_objts(self):
        self.assertIn(User(), models.storage.all().values())

    def test_for_string_with_id_is_public(self):
        self.assertEqual(str, type(User().id))

    def test_for_created_at_is_pblc_date_time(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_for_updated_at_is_pblc_date_time(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_for_email_is_pblc_string(self):
        self.assertEqual(str, type(User.email))

    def test_for_password_is_pblc_string(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_for_last_name_is_pblc_string(self):
        self.assertEqual(str, type(User.last_name))

    def test_for_double_users_with_unique_ids(self):
        User_one_1 = User()
        User_two_2 = User()
        self.assertNotEqual(User_one_1.id, User_two_2.id)

    def test_for_double_users_different_created_at(self):
        User_one_1 = User()
        sleep(0.05)
        User_two_2 = User()
        self.assertLess(User_one_1.created_at, User_two_2.created_at)

    def test_for_double_users_different_updated_at(self):
        User_one_1 = User()
        sleep(0.05)
        User_two_2 = User()
        self.assertLess(User_one_1.updated_at, User_two_2.updated_at)

    def test_for_string_representation(self):
        date_time = datetime.today()
        date_time_repre = repr(date_time)
        User_ = User()
        User_.id = "123456"
        User_.created_at = User_.updated_at = date_time
        User_String = User_.__str__()
        self.assertIn("[User] (123456)", User_String)
        self.assertIn("'id': '123456'", User_String)
        self.assertIn("'created_at': " + date_time_repre, User_String)
        self.assertIn("'updated_at': " + date_time_repre, User_String)

    def test_for_unused_arguments(self):
        User_ = User(None)
        self.assertNotIn(None, User_.__dict__.values())

    def test_for_instantiation_with_kwarguments(self):
        date_time = datetime.today()
        date_time_format = date_time.isoformat()
        User_ = User(id="345", created_at=date_time_format, updated_at=date_time_format)
        self.assertEqual(User_.id, "345")
        self.assertEqual(User_.created_at, date_time)
        self.assertEqual(User_.updated_at, date_time)

    def test_for_inst_without_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class Test_User_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

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
        User_ = User()
        sleep(0.05)
        first_updated_at = User_.updated_at
        User_.save()
        self.assertLess(first_updated_at, User_.updated_at)

    def test_for_double_saves(self):
        User_ = User()
        sleep(0.05)
        first_updated_at = User_.updated_at
        User_.save()
        second_updated_at = User_.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        User_.save()
        self.assertLess(second_updated_at, User_.updated_at)

    def test_for_save_with_arguments(self):
        User_ = User()
        with self.assertRaises(TypeError):
            User_.save(None)

    def test_for_save_updates_file(self):
        User_ = User()
        User_.save()
        User_id_ = "User." + User_.id
        with open("file.json", "r") as f:
            self.assertIn(User_id_, f.read())


class Test_User_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_for_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_for_to_dict_includes_correct_keys(self):
        User_ = User()
        self.assertIn("id", User_.to_dict())
        self.assertIn("created_at", User_.to_dict())
        self.assertIn("updated_at", User_.to_dict())
        self.assertIn("__class__", User_.to_dict())

    def test_for_to_dict_includes_added_attrs(self):
        User_ = User()
        User_.middle_name = "Holberton"
        User_.my_number = 98
        self.assertEqual("Holberton", User_.middle_name)
        self.assertIn("my_number", User_.to_dict())

    def test_for_to_dict_date_time_attrs_are_strings(self):
        User_ = User()
        User_diction = User_.to_dict()
        self.assertEqual(str, type(User_diction["id"]))
        self.assertEqual(str, type(User_diction["created_at"]))
        self.assertEqual(str, type(User_diction["updated_at"]))

    def test_for_to_dict_opt(self):
        date_time = datetime.today()
        User_ = User()
        User_.id = "123456"
        User_.created_at = User_.updated_at = date_time
        Time_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(User_.to_dict(), Time_dict)

    def test_for_comparaison_to_dict_dunder_dict(self):
        User_ = User()
        self.assertNotEqual(User_.to_dict(), User_.__dict__)

    def test_for_to_dict_with_arguments(self):
        User_ = User()
        with self.assertRaises(TypeError):
            User_.to_dict(None)

if __name__ == "__main__":
    unittest.main()

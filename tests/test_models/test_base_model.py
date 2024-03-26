#!/usr/bin/python3
"""Specifies unit tests for models/base_model.py.

Test classes included:
- Test_BaseModel
- Test_BaseModel_save
- Test_BaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_with_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_with_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_with_id_is_public(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_with_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_with_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_with_ids(self):
        base_mo1 = BaseModel()
        base_mo2 = BaseModel()
        self.assertNotEqual(base_mo1.id, base_mo2.id)

    def test_models_with_different_created_at(self):
        base_mo1 = BaseModel()
        sleep(0.05)
        base_mo2 = BaseModel()
        self.assertLess(base_mo1.created_at, base_mo2.created_at)

    def test_models_with_different_updated_at(self):
        base_mo1 = BaseModel()
        sleep(0.05)
        base_mo2 = BaseModel()
        self.assertLess(base_mo1.updated_at, base_mo2.updated_at)

    def test_str_with_representation(self):
        date_tim = datetime.today()
        date_rep = repr(date_tim)
        base_mo = BaseModel()
        base_mo.id = "123456"
        base_mo.created_at = base_mo.updated_at = date_tim
        base_mo_str = base_mo.__str__()
        self.assertIn("[BaseModel] (123456)", base_mo_str)
        self.assertIn("'id': '123456'", base_mo_str)
        self.assertIn("'created_at': " + date_rep, base_mo_str)
        self.assertIn("'updated_at': " + date_rep, base_mo_str)

    def test_for_unused_args(self):
        base_mo = BaseModel(None)
        self.assertNotIn(None, base_mo.__dict__.values())

    def test_for_kwargs_inst(self):
        date_time = datetime.today()
        date_iso = date_time.isoformat()
        base_mo = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base_mo.id, "345")
        self.assertEqual(base_mo.created_at, date_time)
        self.assertEqual(base_mo.updated_at, date_time)

    def test_for_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_for_args_and_kwargs(self):
        date_time = datetime.today()
        date_iso = date_time.isoformat()
        base_mo = BaseModel("12", id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base_mo.id, "345")
        self.assertEqual(base_mo.created_at, date_time)
        self.assertEqual(base_mo.updated_at, date_time)


class Test_BaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_for_onesave(self):
        base_mod = BaseModel()
        sleep(0.05)
        first_updated_at = base_mod.updated_at
        base_mod.save()
        self.assertLess(first_updated_at, base_mod.updated_at)

    def test_for_double_save(self):
        base_mod = BaseModel()
        sleep(0.05)
        first_updated_at = base_mod.updated_at
        base_mod.save()
        second_updated_at = base_mod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base_mod.save()
        self.assertLess(second_updated_at, base_mod.updated_at)

    def test_and_save_with_argument(self):
        base_mod = BaseModel()
        with self.assertRaises(TypeError):
            base_mod.save(None)

    def test_and_save_for_updates_file(self):
        base_mo = BaseModel()
        base_mo.save()
        base_mo_id = "BaseModel." + base_mo.id
        with open("file.json", "r") as f:
            self.assertIn(base_mo_id, f.read())


class Test_BaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dictype(self):
        base_mod = BaseModel()
        self.assertTrue(dict, type(base_mod.to_dict()))

    def test_to_dict_with_correct_keys(self):
        base_mod = BaseModel()
        self.assertIn("id", base_mod.to_dict())
        self.assertIn("created_at", base_mod.to_dict())
        self.assertIn("updated_at", base_mod.to_dict())
        self.assertIn("__class__", base_mod.to_dict())

    def test_for_to_dict_with_added_attributes(self):
        base_mo = BaseModel()
        base_mo.name = "Holberton"
        base_mo.my_number = 98
        self.assertIn("name", base_mo.to_dict())
        self.assertIn("my_number", base_mo.to_dict())

    def test_for_to_dict_datetime_attributes(self):
        base_mo = BaseModel()
        base_mo_dict = base_mo.to_dict()
        self.assertEqual(str, type(base_mo_dict["created_at"]))
        self.assertEqual(str, type(base_mo_dict["updated_at"]))

    def test_for_to_dict_output(self):
        date_tim = datetime.today()
        base_mo = BaseModel()
        base_mo.id = "123456"
        base_mo.created_at = base_mo.updated_at = date_tim
        tim_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date_tim.isoformat(),
            'updated_at': date_tim.isoformat()
        }
        self.assertDictEqual(base_mo.to_dict(), tim_dict)

    def test_for_contrast_to_dict_dundict(self):
        base_mo = BaseModel()
        self.assertNotEqual(base_mo.to_dict(), base_mo.__dict__)

    def test_for_to_dict_with_args(self):
        base_mo = BaseModel()
        with self.assertRaises(TypeError):
            base_mo.to_dict(None)


if __name__ == "__main__":
    unittest.main()

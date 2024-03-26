#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    Test_FileStorage_instantiation
    Test_FileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_FileStorage_inst(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_for_FileStorage_inst_without_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_for_FileStorage_inst_with_arguments(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_for_FileStorage_file_path_is_prvt_string(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_fot_FileStorage_objts_is_private_dictionair(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_for_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_for_all_funct(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_for_all_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_for_new_func(self):
        Base_Model_ = BaseModel()
        Us__er = User()
        Sta__te = State()
        Pla__ce = Place()
        Ci__ty = City()
        Ame__nity = Amenity()
        Rev__iew = Review()
        models.storage.new(Base_Model_)
        models.storage.new(Us__er)
        models.storage.new(Sta__te)
        models.storage.new(Pla__ce)
        models.storage.new(Ci__ty)
        models.storage.new(Ame__nity)
        models.storage.new(Rev__iew)
        self.assertIn("BaseModel." + Base_Model_.id, models.storage.all().keys())
        self.assertIn(Base_Model_, models.storage.all().values())
        self.assertIn("User." + Us__er.id, models.storage.all().keys())
        self.assertIn(Us__er, models.storage.all().values())
        self.assertIn("State." + Sta__te.id, models.storage.all().keys())
        self.assertIn(Sta__te, models.storage.all().values())
        self.assertIn("Place." + Pla__ce.id, models.storage.all().keys())
        self.assertIn(Pla__ce, models.storage.all().values())
        self.assertIn("City." + Ci__ty.id, models.storage.all().keys())
        self.assertIn(Ci__ty, models.storage.all().values())
        self.assertIn("Amenity." + Ame__nity.id, models.storage.all().keys())
        self.assertIn(Ame__nity, models.storage.all().values())
        self.assertIn("Review." + Rev__iew.id, models.storage.all().keys())
        self.assertIn(Rev__iew, models.storage.all().values())

    def test_for_new_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_for_save_function(self):
        Base_Model_ = BaseModel()
        Us__er = User()
        Sta__te = State()
        Pla__ce = Place()
        Ci__ty = City()
        Ame__nity = Amenity()
        Rev__iew = Review()
        models.storage.new(Base_Model_)
        models.storage.new(Us__er)
        models.storage.new(Sta__te)
        models.storage.new(Pla__ce)
        models.storage.new(Ci__ty)
        models.storage.new(Ame__nity)
        models.storage.new(Rev__iew)
        models.storage.save()
        SaveText_ = ""
        with open("file.json", "r") as file:
            SaveText_ = file.read()
            self.assertIn("BaseModel." + Base_Model_.id, SaveText_)
            self.assertIn("User." + Us__er.id, SaveText_)
            self.assertIn("State." + Sta__te.id, SaveText_)
            self.assertIn("Place." + Pla__ce.id, SaveText_)
            self.assertIn("City." + Ci__ty.id, SaveText_)
            self.assertIn("Amenity." + Ame__nity.id, SaveText_)
            self.assertIn("Review." + Rev__iew.id, SaveText_)

    def test_for_save_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_for_reload_function(self):
        Base_Model_ = BaseModel()
        Us__er = User()
        Sta__te = State()
        Pla__ce = Place()
        Ci__ty = City()
        Ame__nity = Amenity()
        Rev__iew = Review()
        models.storage.new(Base_Model_)
        models.storage.new(Us__er)
        models.storage.new(Sta__te)
        models.storage.new(Pla__ce)
        models.storage.new(Ci__ty)
        models.storage.new(Ame__nity)
        models.storage.new(Rev__iew)
        models.storage.save()
        models.storage.reload()
        Obje_cts = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + Base_Model_.id, Obje_cts)
        self.assertIn("User." + Us__er.id, Obje_cts)
        self.assertIn("State." + Sta__te.id, Obje_cts)
        self.assertIn("Place." + Pla__ce.id, Obje_cts)
        self.assertIn("City." + Ci__ty.id, Obje_cts)
        self.assertIn("Amenity." + Ame__nity.id, Obje_cts)
        self.assertIn("Review." + Rev__iew.id, Obje_cts)

    def test_for_reload_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

if __name__ == "__main__":
    unittest.main()

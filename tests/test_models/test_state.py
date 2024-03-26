#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateInstanceCreation
    TestStateSaveMethod
    TestStateToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateInstanceCreation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_without_instan(self):
        self.assertEqual(State, type(State()))

    def test_for_new_instance_stored_in_objts(self):
        self.assertIn(State(), models.storage.all().values())

    def test_for_id_is_public_strings(self):
        self.assertEqual(str, type(State().id))

    def test_for_created_at_is_public_date_time(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_for_updated_at_is_public_date_time(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_for_name_is_public_cls_attr(self):
        StateEObject = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(StateEObject))
        self.assertNotIn("name", StateEObject.__dict__)

    def test_for_two_states_with_unique_id(self):
        State_One_1 = State()
        State_One_2 = State()
        self.assertNotEqual(State_One_1.id, State_One_2.id)

    def test_for_double_states_different_created_at(self):
        State_One_1 = State()
        sleep(0.05)
        State_One_2 = State()
        self.assertLess(State_One_1.created_at, State_One_2.created_at)

    def test_for_double_states_different_updated_at(self):
        State_One_1 = State()
        sleep(0.05)
        State_One_2 = State()
        self.assertLess(State_One_1.updated_at, State_One_2.updated_at)

    def test_for_string_repres(self):
        date_time = datetime.today()
        date_represnt = repr(date_time)
        StateEObject = State()
        StateEObject.id = "123456"
        StateEObject.created_at = StateEObject.updated_at = date_time
        state_str = StateEObject.__str__()
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': " + date_represnt, state_str)
        self.assertIn("'updated_at': " + date_represnt, state_str)

    def test_for_unused_args(self):
        StateEObject = State(None)
        self.assertNotIn(None, StateEObject.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        date_format_iso = date_time.isoformat()
        StateEObject = State(id="345", created_at=date_format_iso, updated_at=date_format_iso)
        self.assertEqual(StateEObject.id, "345")
        self.assertEqual(StateEObject.created_at, date_time)
        self.assertEqual(StateEObject.updated_at, date_time)

    def test_inst_without_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSaveMethod(unittest.TestCase):
    """Unittests for testing save method of the State class."""

    @classmethod
    def setUpClass(cls):
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

    def test_for_1_save(self):
        StateEObject = State()
        sleep(0.05)
        first_updated_at = StateEObject.updated_at
        StateEObject.save()
        self.assertLess(first_updated_at, StateEObject.updated_at)

    def test_for_2_saves(self):
        StateEObject = State()
        sleep(0.05)
        first_updated_at = StateEObject.updated_at
        StateEObject.save()
        second_updated_at = StateEObject.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        StateEObject.save()
        self.assertLess(second_updated_at, StateEObject.updated_at)

    def test_for_save_with_arguments(self):
        StateEObject = State()
        with self.assertRaises(TypeError):
            StateEObject.save(None)

    def test_for_save_updated_file(self):
        StateEObject = State()
        StateEObject.save()
        StateId_ = "State." + StateEObject.id
        with open("file.json", "r") as f:
            self.assertIn(StateId_, f.read())


class TestStateToDictMethod(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_for_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_for_to_dict_includes_correct_keys(self):
        StateEObject = State()
        self.assertIn("id", StateEObject.to_dict())
        self.assertIn("created_at", StateEObject.to_dict())
        self.assertIn("updated_at", StateEObject.to_dict())
        self.assertIn("__class__", StateEObject.to_dict())

    def test_for_to_dict_includes_added_attr(self):
        StateEObject = State()
        StateEObject.middle_name = "Holberton"
        StateEObject.my_number = 98
        self.assertEqual("Holberton", StateEObject.middle_name)
        self.assertIn("my_number", StateEObject.to_dict())

    def test_for_to_dict_date_time_attr_are_strings(self):
        StateEObject = State()
        StateDiction_ = StateEObject.to_dict()
        self.assertEqual(str, type(StateDiction_["id"]))
        self.assertEqual(str, type(StateDiction_["created_at"]))
        self.assertEqual(str, type(StateDiction_["updated_at"]))

    def test_for_to_dict_opt(self):
        date_time = datetime.today()
        StateEObject = State()
        StateEObject.id = "123456"
        StateEObject.created_at = StateEObject.updated_at = date_time
        time_diction = {
            'id': '123456',
            '__class__': 'State',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(StateEObject.to_dict(), time_diction)

    def test_for_comparison_to_dict_and_dunder_dict(self):
        StateEObject = State()
        self.assertNotEqual(StateEObject.to_dict(), StateEObject.__dict__)

    def test_for_to_dict_conatains_argumnets(self):
        StateEObject = State()
        with self.assertRaises(TypeError):
            StateEObject.to_dict(None)


if __name__ == "__main__":
    unittest.main()

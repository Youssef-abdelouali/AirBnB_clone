#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_initialization(self):
        """Test initialization of State."""
        # Verify if a State instance is created successfully
        state = State()
        self.assertIsInstance(state, State)

        # Test if default values for attributes are correctly set
        self.assertEqual(state.name, "")

        # Verify that State instances have unique ids
        state_2 = State()
        self.assertNotEqual(state.id, state_2.id)

    def test_attribute_assignment(self):
        """Test attribute assignment of State."""
        # Test if attributes are properly assigned
        state = State(
            name="California"
        )
        self.assertEqual(state.name, "California")

    def test_attribute_types(self):
        """Test attribute types of State."""
        # Test if attributes have correct types
        state = State()
        self.assertIsInstance(state.name, str)

    def test_edge_cases(self):
        """Test edge cases for attribute assignment."""
        # Test assigning empty string to attribute
        state = State(
            name=""
        )
        self.assertEqual(state.name, "")

        # Test assigning None value to attribute
        state = State(
            name=None
        )
        self.assertIsNone(state.name)

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple State instances."""
        # Verify that State instances have unique ids
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        state = State(
            name="California"
        )
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "California")

        # Test deserialization
        new_state = State(**state_dict)
        self.assertEqual(new_state.name, "California")

if __name__ == "__main__":
    unittest.main()

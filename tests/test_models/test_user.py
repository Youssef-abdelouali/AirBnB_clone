#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_initialization(self):
        """Test initialization of User."""
        # Verify if a User instance is created successfully
        user = User()
        self.assertIsInstance(user, User)

        # Test if default values for attributes are correctly set
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        # Verify that User instances have unique ids
        user_2 = User()
        self.assertNotEqual(user.id, user_2.id)

    def test_attribute_assignment(self):
        """Test attribute assignment of User."""
        # Test if email, password, first_name, and last_name attributes are properly assigned
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_attribute_edge_cases(self):
        """Test edge cases for attribute assignment."""
        # Test assigning empty strings to attributes
        user = User(email="", password="", first_name="", last_name="")
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        # Test assigning None values to attributes
        user = User(email=None, password=None, first_name=None, last_name=None)
        self.assertIsNone(user.email)
        self.assertIsNone(user.password)
        self.assertIsNone(user.first_name)
        self.assertIsNone(user.last_name)

        # Test assigning invalid types to attributes
        with self.assertRaises(TypeError):
            user = User(email=123, password=456, first_name=789, last_name=True)

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple User instances."""
        # Verify that User instances have unique ids
        user_1 = User()
        user_2 = User()
        self.assertNotEqual(user_1.id, user_2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

        # Test deserialization
        new_user = User(**user_dict)
        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "password")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")

if __name__ == "__main__":
    unittest.main()

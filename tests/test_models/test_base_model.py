#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init_with_no_arguments(self):
        """Test initialization of BaseModel with no arguments."""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init_with_arguments_and_kwargs(self):
        """Test initialization of BaseModel with arguments and keyword arguments."""
        base_model = BaseModel("arg1", key1="value1")
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init_with_invalid_arguments(self):
        """Test initialization of BaseModel with invalid arguments."""
        with self.assertRaises(TypeError):
            BaseModel(123)

    def test_unique_ids(self):
        """Test uniqueness of ids for BaseModel instances."""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        base_model = BaseModel()
        base_model.name = "Test Model"
        base_model.my_number = 42
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['name'], "Test Model")
        self.assertEqual(base_model_dict['my_number'], 42)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        base_model = BaseModel()
        self.assertIn("BaseModel", str(base_model))
        self.assertIn(base_model.id, str(base_model))
        self.assertIn(str(base_model.__dict__), str(base_model))

    def test_modify_created_updated_attributes(self):
        """Test modifying created_at and updated_at attributes."""
        base_model = BaseModel()
        base_model.created_at = datetime(2020, 1, 1)
        base_model.updated_at = datetime(2021, 1, 1)
        base_model_dict = base_model.to_dict()

        self.assertEqual(base_model_dict['created_at'], '2020-01-01T00:00:00')
        self.assertEqual(base_model_dict['updated_at'], '2021-01-01T00:00:00')

    def test_invalid_attribute_types(self):
        """Test invalid attribute types."""
        with self.assertRaises(TypeError):
            BaseModel(name=123)

    def test_behavior_with_multiple_instances(self):
        """Test behavior with multiple BaseModel instances."""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_serialization_deserialization(self):
        """Test serialization and deserialization."""
        # Test serialization
        base_model = BaseModel(
            name="Test Model",
            my_number=42
        )
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['name'], "Test Model")
        self.assertEqual(base_model_dict['my_number'], 42)

        # Test deserialization
        new_base_model = BaseModel(**base_model_dict)
        self.assertEqual(new_base_model.name, "Test Model")
        self.assertEqual(new_base_model.my_number, 42)

if __name__ == "__main__":
    unittest.main()

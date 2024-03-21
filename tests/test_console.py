
#!/usr/bin/python3
"""Defines unit tests for console.py.

Unit test classes include:

TestHBNBCommand_prompting
TestHBNBCommand_help
TestHBNBCommand_exit
TestHBNBCommand_create
TestHBNBCommand_show
TestHBNBCommand_all
TestHBNBCommand_destroy
TestHBNBCommand_update

"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBConsole
from io import StringIO
from unittest.mock import patch

class TestHBNBConsole(unittest.TestCase):
    """Test cases for HBNBConsole class."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBConsole()

    def tearDown(self):
        """Tear down the test environment."""
        del self.console

    def test_create_instance(self):
        """Test creating a new instance."""
        # Test creating a new instance of a valid class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if id is generated

        # Test creating an instance of an invalid class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_instance(self):
        """Test showing an instance."""
        # Test showing an existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            id_output = fake_out.getvalue().strip()
            self.console.onecmd(f"show BaseModel {id_output}")
            show_output = fake_out.getvalue().strip()
            self.assertNotEqual(show_output, "** no instance found **")

        # Test showing an instance of a non-existing class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show InvalidClass 12345")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        # Test showing an instance with missing class name
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        # Test showing an instance with missing instance id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        # Add more test cases for show command...

    def test_destroy_instance(self):
        """Test destroying an instance."""
        # Test destroying an existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            id_output = fake_out.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {id_output}")
            self.console.onecmd(f"show BaseModel {id_output}")
            show_output = fake_out.getvalue().strip()
            self.assertEqual(show_output, "** no instance found **")

        # Test destroying a non-existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel 12345")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

        # Test destroying an instance with missing class name
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        # Test destroying an instance with missing instance id
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        # Add more test cases for destroy command...

    def test_all_instances(self):
        """Test displaying all instances."""
        # Test displaying all instances of a specific class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            all_output = fake_out.getvalue().strip()
            self.assertTrue(len(all_output) > 0)  # Check if output is not empty

        # Test displaying all instances without specifying a class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            all_output = fake_out.getvalue().strip()
            self.assertTrue(len(all_output) > 0)  # Check if output is not empty

        # Test displaying all instances of a non-existing class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        

    def test_count_instances(self):
        """Test counting instances."""
        # Test counting instances of a specific class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            count_output = fake_out.getvalue().strip()
            self.assertEqual(count_output, "3")

        # Test counting instances without specifying a class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        # Test counting instances of a non-existing class
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("count InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        # Add more test cases for count command...

    def test_update_instance(self):
        """Test updating an instance."""
        # Test updating an instance's attribute
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            id_output = fake_out.getvalue().strip()
            self.console.onecmd(f"update BaseModel {id_output} name 'New Name'")
            self.console.onecmd(f"show BaseModel {id_output}")
            show_output = fake_out.getvalue().strip()
            self.assertIn("'name': 'New Name'", show_output)

        # Test updating an instance's attribute with invalid value
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            id_output = fake_out.getvalue().strip()
            self.console.onecmd(f"update BaseModel {id_output} name 123")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** value missing **")

        # Test updating an attribute of a non-existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel 12345 name 'New Name'")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
    

    def test_quit_command(self):
        """Test quitting the program."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue().strip(), "")

    def test_EOF_command(self):
        """Test handling EOF signal."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue().strip(), "")

    def test_help_command(self):
        """Test displaying help message."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.console.onecmd("help"))
            self.assertIn("Documented commands (type help <topic>):", fake_out.getvalue())

    # Add more test cases...

    def test_prompt(self):
        """Test command prompt."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.cmdloop()
            self.assertEqual(fake_out.getvalue().strip(), "(hbnb) ")

    def test_invalid_command(self):
        """Test handling invalid command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.console.onecmd("invalid_command"))
            self.assertIn("*** Unknown syntax: invalid_command", fake_out.getvalue())

    
if __name__ == "__main__":
    unittest.main()

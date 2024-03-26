#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    Test_HBNBCommand_prompting
    Test_HBNBCommand_help
    Test_HBNBCommand_exit
    Test_HBNBCommand_create
    Test_HBNBCommand_show
    Test_HBNBCommand_all
    Test_HBNBCommand_destroy
    Test_HBNBCommand_update
"""
import os
import sys
import unittest
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from io import StringIO


class Test_HBNB_Command_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB Comm_and_ interpreter."""

    def test_for_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_for_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class Test_HBNB_Command_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB Comm_and_ interpreter."""

    def test_for_help_quit_command(self):
        Hel__p = "Quit Comm_and_ to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_create_command(self):
        Hel__p = ("Usage: create <class>\n        "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_EOF_command(self):
        Hel__p = "Signal to exit the program upon reaching EOF.."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_show_command(self):
        Hel__p = ("Usage: show <class> <id> or <class>.show(<id>)\n        "
             "Display the string representation of a class instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_destroy_command(self):
        Hel__p = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n        "
             "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_all_command(self):
        Hel__p = ("Usage: all or all <class> or <class>.all()\n        "
             "Display string representations of all instances of a given class"
             ".\n        If no class is specified, displays all instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_count_command(self):
        Hel__p = ("Usage: count <class> or <class>.count()\n        "
             "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help_update_command(self):
        Hel__p = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n       <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n       <class>.update(<id>, <dictionary>)\n        "
             "Update a class instance of a given id by adding or updating\n   "
             "     a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(Hel__p, output.getvalue().strip())

    def test_for_help(self):
        Hel__p = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(Hel__p, output.getvalue().strip())


class Test_HBNB_Command_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB Comm_and_ interpreter."""

    def test_for_quit_exits_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_for_EOF_exits_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class Test_HBNB_Command_create(unittest.TestCase):
    """Unittests for testing create from the HBNB Comm_and_ interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_for_create_missing_a_class(self):
        Corr__ect = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_create_invalid_a_class(self):
        Corr__ect = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_create_invalid_a_syntax(self):
        Corr__ect = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        Corr__ect = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_create_an_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "User.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "State.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "City.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            Test_Key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(Test_Key, storage.all().keys())


class Test_HBNB_Command_show(unittest.TestCase):
    """Unittests for testing show from the HBNB Comm_and_ interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_for_show_a_missing_class(self):
        Corr__ect = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_an_invalid_class(self):
        Corr__ect = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_a_missing_id_space_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_a_missing_id_dot_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_no_instance_find_space_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_no_instance_find_dot_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.show(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_show_objcts_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["BaseModel.{}".format(Test_ID_)]
            Comm_and_ = "show BaseModel {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["User.{}".format(Test_ID_)]
            Comm_and_ = "show User {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["State.{}".format(Test_ID_)]
            Comm_and_ = "show State {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Place.{}".format(Test_ID_)]
            Comm_and_ = "show Place {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["City.{}".format(Test_ID_)]
            Comm_and_ = "show City {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Amenity.{}".format(Test_ID_)]
            Comm_and_ = "show Amenity {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Review.{}".format(Test_ID_)]
            Comm_and_ = "show Review {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())

    def test_for_show_objts_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["BaseModel.{}".format(Test_ID_)]
            Comm_and_ = "BaseModel.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["User.{}".format(Test_ID_)]
            Comm_and_ = "User.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["State.{}".format(Test_ID_)]
            Comm_and_ = "State.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Place.{}".format(Test_ID_)]
            Comm_and_ = "Place.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["City.{}".format(Test_ID_)]
            Comm_and_ = "City.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Amenity.{}".format(Test_ID_)]
            Comm_and_ = "Amenity.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Review.{}".format(Test_ID_)]
            Comm_and_ = "Review.show({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertEqual(Obje_ct.__str__(), output.getvalue().strip())


class Test_HBNB_Command_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB Comm_and_ interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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
        storage.reload()

    def test_for_destroy_a_missing_class(self):
        Corr__ect = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_invalid_class(self):
        Corr__ect = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_id_missing_space_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_id_missing_dot_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_invalid_id_space_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_invalid_id_dot_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_destroy_an_objts_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["BaseModel.{}".format(Test_ID_)]
            Comm_and_ = "destroy BaseModel {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["User.{}".format(Test_ID_)]
            Comm_and_ = "show User {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["State.{}".format(Test_ID_)]
            Comm_and_ = "show State {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Place.{}".format(Test_ID_)]
            Comm_and_ = "show Place {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["City.{}".format(Test_ID_)]
            Comm_and_ = "show City {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Amenity.{}".format(Test_ID_)]
            Comm_and_ = "show Amenity {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Review.{}".format(Test_ID_)]
            Comm_and_ = "show Review {}".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())

    def test_for_destroy_objts_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["BaseModel.{}".format(Test_ID_)]
            Comm_and_ = "BaseModel.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["User.{}".format(Test_ID_)]
            Comm_and_ = "User.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["State.{}".format(Test_ID_)]
            Comm_and_ = "State.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Place.{}".format(Test_ID_)]
            Comm_and_ = "Place.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["City.{}".format(Test_ID_)]
            Comm_and_ = "City.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Amenity.{}".format(Test_ID_)]
            Comm_and_ = "Amenity.destroy({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Obje_ct = storage.all()["Review.{}".format(Test_ID_)]
            Comm_and_ = "Review.destory({})".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Comm_and_))
            self.assertNotIn(Obje_ct, storage.all())


class Test_HBNB_Command_all(unittest.TestCase):
    """Unittests for testing all of the HBNB Comm_and_ interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_for_all_an_invalid_class(self):
        Corr__ect = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_all_objts_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_for_all_objts_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_for_all_single_objct_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_for_all_single_objt_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class Test_HBNB_Command_update(unittest.TestCase):
    """Unittests for testing update from the HBNB Comm_and_ interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

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

    def test_for_update_with_missing_class(self):
        Corr__ect = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_with_invalid_class(self):
        Corr__ect = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_a_missing_id_with_space_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_missing_id_with_dot_notation(self):
        Corr__ect = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update()"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_invalid_id_with_space_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_invalid_id_with_dot_notation(self):
        Corr__ect = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.update(1)"))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_a_missing_attr_with_name_space_notation(self):
        Corr__ect = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update BaseModel {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update User {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update State {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update City {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update Amenity {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "update Place {}".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_missing_attr_name_with_dot_notation(self):
        Corr__ect = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "BaseModel.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "User.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "State.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "City.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "Amenity.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Test_ID_ = output.getvalue().strip()
            Test_Cmd_ = "Place.update({})".format(Test_ID_)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_missing_attr_value_with_space_notation(self):
        Corr__ect = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update BaseModel {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update User {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update State {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update City {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update Amenity {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update Place {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "update Review {} attr_name".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_missing_attr_value_with_dot_notation(self):
        Corr__ect = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "BaseModel.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "User.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "State.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "City.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "Amenity.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "Place.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            Test_Cmd_ = "Review.update({}, attr_name)".format(Test_ID_)
            self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
            self.assertEqual(Corr__ect, output.getvalue().strip())

    def test_for_update_valid_string_attr_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update BaseModel {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["BaseModel.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update User {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["User.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update State {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["State.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update City {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["City.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Amenity {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Amenity.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Review {} attr_name 'attr_value'".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Review.{}".format(Test_ID_)].__dict__
        self.assertTrue("attr_value", Test_Diction["attr_name"])

    def test_for_update_valid_string_attr_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "BaseModel.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["BaseModel.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "User.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["User.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "State.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["State.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "City.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["City.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Amenity.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Amenity.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Review.update({}, attr_name, 'attr_value')".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Review.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

    def test_for_update_valid_int_attr_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} max_guest 98".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(98, Test_Diction["max_guest"])

    def test_for_update_valid_int_attr_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, max_guest, 98)".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(98, Test_Diction["max_guest"])

    def test_for_update_valid_float_attr_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} latitude 7.2".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(7.2, Test_Diction["latitude"])

    def test_for_update_valid_float_attr_with_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, latitude, 7.2)".format(Test_ID_)
        self.assertFalse(HBNBCommand().onecmd(Test_Cmd_))
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(7.2, Test_Diction["latitude"])

    def test_for_update_valid_dictionary_with_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update BaseModel {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["BaseModel.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update User {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["User.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update State {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["State.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update City {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["City.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Amenity {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Amenity.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Review {} ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'}"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Review.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "BaseModel.update({}".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["BaseModel.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "User.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["User.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "State.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["State.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "City.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["City.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Amenity.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Amenity.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Review.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'attr_name': 'attr_value'})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Review.{}".format(Test_ID_)].__dict__
        self.assertEqual("attr_value", Test_Diction["attr_name"])

    def test_for_update_valid_dictionary_with_int__space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} ".format(Test_ID_)
        Test_Cmd_ += "{'max_guest': 98})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(98, Test_Diction["max_guest"])

    def test_for_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'max_guest': 98})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(98, Test_Diction["max_guest"])

    def test_for_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "update Place {} ".format(Test_ID_)
        Test_Cmd_ += "{'latitude': 9.8})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(9.8, Test_Diction["latitude"])

    def test_forr_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Test_ID_ = output.getvalue().strip()
        Test_Cmd_ = "Place.update({}, ".format(Test_ID_)
        Test_Cmd_ += "{'latitude': 9.8})"
        HBNBCommand().onecmd(Test_Cmd_)
        Test_Diction = storage.all()["Place.{}".format(Test_ID_)].__dict__
        self.assertEqual(9.8, Test_Diction["latitude"])


class Test_HBNB_Command_count_(unittest.TestCase):
    """Unittests for testing count method of HBNB comand interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

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

    def test_for_that_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_for_count_objt(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())
if __name__ == "__main__":
    unittest.main()

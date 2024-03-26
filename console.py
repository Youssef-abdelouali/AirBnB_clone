#!/usr/bin/python3
"""HolbertonBnB console for managing objects."""
import cmd
import re
from shlex import split 
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_input(arg):
    """Parse the input arguments."""
    Curly_Braces_Match = re.search(r"\{(.*?)\}", arg)
    Brac_kets_Match = re.search(r"\[(.*?)\]", arg)
    if Curly_Braces_Match is None:
        if Brac_kets_Match is None:
            return [i.strip(",") for i in split(arg)]
        else:
            Lex_er_ = split(arg[:Brac_kets_Match.span()[0]])
            result_list = [i.strip(",") for i in Lex_er_]
            result_list.append(Brac_kets_Match.group())
            return result_list
    else:
        Lex_er_ = split(arg[:Curly_Braces_Match.span()[0]])
        result_list = [i.strip(",") for i in Lex_er_]
        result_list.append(Curly_Braces_Match.group())
        return result_list


class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command line interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def handle_empty_line(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior when input is invalid."""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Signal to exit the program upon reaching EOF."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of a class and print its id.

        Usage: create <class>
        """
        arg_list = parse_input(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.__classes[arg_list[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Display the string representation of an instance.

        Usage: show <class> <id> or <class>.show(<id>)
        """
        arg_list = parse_input(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id.

        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        arg_list = parse_input(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Display all instances or instances of a specific class.

        Usage: all or all <class> or <class>.all()
        """
        arg_list = parse_input(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class.

        Usage: count <class> or <class>.count()
        """
        arg_list = parse_input(arg)
        cou_nter = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                cou_nter += 1
        print(cou_nter)

    def do_update(self, arg):
        """Update an instance with new attribute or value.

        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        """
        arg_list = parse_input(arg)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for x, y in eval(arg_list[2]).items():
                if (x in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[x]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[x])
                    obj.__dict__[x] = valtype(y)
                else:
                    obj.__dict__[x] = y
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    """Function to parse the object"""
    result = []
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    splited_arg = split(arg)
    if not curly_brackets:
        if not square_brackets:
            for i in splited_arg:
                result.append(i.strip(","))
            return result
        else:
            lexer = split(arg[:square_brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(square_brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_brackets.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_brackets.group())
        return retl


CLASSES = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Place',
        'Amenity',
        'Review'
]


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exit the program."""
        return True

    def emptyline(self):
        """Prints nothing after having a blank line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_create(self, argv):
        """
        Usage: create <class>

        Creates a new class instance and print its id
        """
        arg = parse(argv)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, argv):
        """
        Usage: show <class>

        Prints the string rep of instance on the class name and id
        """
        arg = parse(argv)
        all_storage = storage.all()
        if len(arg) > 1:
            class_instance = f"{arg[0]}.{arg[1]}"

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif class_instance not in all_storage:
            print("** no instance found **")
        else:
            print(all_storage[class_instance])

    def do_destroy(self, argv):
        """
        Usage: destroy <class> <id>

        Delete a class instance of a given id.
        """
        arg = parse(argv)
        all_storage = storage.all()
        if len(arg) > 1:
            class_instance = f"{arg[0]}.{arg[1]}"

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif class_instance not in all_storage:
            print("** no instance found **")
        else:
            del all_storage[class_instance]
            storage.save()

    def do_all(self, argv):
        """
        Usage: all or all <class> or <class>.all()

        Displays the string representations of all instances of a given class.

        Displays all instantiated objects if there is no class specification.
        """
        arg = parse(argv)
        if len(arg) > 0 and arg[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            all_objects = []
            for element in storage.all().values():
                if len(arg) >= 0 and arg[0] == element.__class__.__name__:
                    all_objects.append(element.__str__())
            print(all_objects)

    def do_update(self, argv):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value>

        Update a class instance of a given id by adding or updating\
a given attribute key/value pair or dictionary.
        """
        arg = parse(argv)
        arg_len = len(arg)
        all_storage = storage.all()
        class_instance = f"{arg[0]}.{arg[1]}"
        if arg_len == 0:
            print("** class name missing **")
            return False
        if arg[0] not in CLASSES:
            print("** class doesn't exist **")
            return False
        if arg_len == 1:
            print("** instance id missing **")
            return False
        if class_instance not in all_storage.keys():
            print("** no instance found **")
            return False
        if arg_len == 2:
            print("** attribute name missing **")
            return False
        if arg_len == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if arg_len == 4:
            obj = all_storage[class_instance]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            obj = all_storage[class_instance]
            for k, v in eval(arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, argv):
        """
        Usage: count <class> or <class>.count()

        Retrieve the number of instances of a given class.
        """
        arg = parse(argv)
        count = 0
        for element in storage.all().values():
            if arg[0] == element.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

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
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


CLASSES = ['BaseModel']


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def __init__(self):
        """Initialization of the class and calling super"""
        super().__init__()

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

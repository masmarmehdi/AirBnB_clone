#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

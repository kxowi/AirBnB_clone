#!/usr/bin/python3
"""Module that a command line interpreter"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """Airbnb command-line interpreter"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF to exit the program"""
        print("")
        return (True)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return (True)

    def do_create(self, line):
        """Create an instance and save it"""
        if not line:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            instance = classes[line]()
            print(instance.id)
            instance.save()

    def do_show(self, line):
        """Show an instance via its id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            obj = f"{args[0]}.{args[1]}"
            if obj not in all_objects:
                print("** no instance found **")
            else:
                for k, v in storage.all().items():
                    if k.split(".")[1] == args[1]:
                        print(v)
                        return

    def do_destroy(self, line):
        """Destroy an instance via its id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            obj = f"{args[0]}.{args[1]}"
            if obj not in all_objects:
                print("** no instance found **")
            else:
                for k, v in storage.all().items():
                    if k.split(".")[1] == args[1]:
                        del storage.all()[k]
                        storage.save()
                        return

    def do_all(self, line):
        """Print all instances as string representation"""
        args = line.split()
        string = []
        if len(args) == 0:
            for v in storage.all().values():
                string.append(str(v))
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            for k, v in storage.all().items():
                if k.split(".")[0] == args[0]:
                    string.append(str(v))
        if len(string) > 0:
            print(string)

    def do_update(self, line):
        """Update an instance's attribute"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_objects = storage.all()
            obj = f"{args[0]}.{args[1]}"
            if obj not in all_objects:
                print("** no instance found **")
            else:
                if args[2] not in ["id", "created_at", "updated_at"]:
                    my_inst = all_objects[obj]
                    if args[3].startswith('"') and args[3].endswith('"'):
                        args[3] = args[3][1:-1]
                    if hasattr(my_inst, args[2]):
                        type_att = type(getattr(my_inst, args[2]))
                        setattr(my_inst, args[2], type_att(args[3]))
                    else:
                        setattr(my_inst, args[2], args[3])
                    my_inst.save()

    def emptyline(self):
        """ENTER with empty line should not do anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

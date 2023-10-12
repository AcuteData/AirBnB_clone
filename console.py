#!/usr/bin/python3
""" Console """

import cmd
from datetime import datetime
from models import Amenity, BaseModel, City, Place, Review, State, User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNB console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exits console """
        return True

    def emptyline(self):
        """ Overriding the emptyline method """
        return False

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def _key_value_parser(self, args):
        """ Creates a dictionary from a list of strings """
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """ Creates a new instance of a class """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[class_name](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ Prints an instance as a string based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name in classes:
            if len(args) > 1:
                instance_id = args[1]
                key = class_name + "." + instance_id
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                instance_id = args[1]
                key = args[0] + "." + instance_id
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints string representations of instances """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """ Update an instance based on the class name, id, attribute & value """
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                instance_id = args[1]
                key = args[0] + "." + instance_id
                if key in models.storage.all():
                    if len(args) > 2:
                        attribute_name = args[2]
                        if len(args) > 3:
                            attribute_value = args[3]
                            if args[0] == "Place":
                                if attribute_name in integers:
                                    try:
                                        attribute_value = int(attribute_value)
                                    except ValueError:
                                        attribute_value = 0
                                elif attribute_name in floats:
                                    try:
                                        attribute_value = float(attribute_value)
                                    except ValueError:
                                        attribute_value = 0.0
                            setattr(models.storage.all()[key], attribute_name, attribute_value)
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

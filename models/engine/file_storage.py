import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    # Path to the JSON file
    __file_path = "file.json"
    # Dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    filtered_dict[key] = value
            return filtered_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                json_data = json.load(file)
            for key in json_data:
                self.__objects[key] = class_dict[json_data[key]["__class__"]](**json_data[key])
        except:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Retrieves one object based on the class name and its ID
        Attributes:
            cls (string): string representing the class name
            id (string): string representing the object ID
        Return: the object, or None if not found
        """
        if cls is not None:
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    if value.id == id:
                        return value
        return None

    def count(self, cls=None):
        """Returns the number of objects in storage matching the given class name
        Returns count of all objects in storage if no class name given
        Attributes:
            cls (string): string representing the class name (optional)
        Return: the number of objects in storage
        """
        count = 0
        if cls is not None:
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    count += 1
            return count
        return len(self.__objects)

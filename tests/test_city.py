#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import city
from models.base_model import BaseModel
import pep8
import unittest
City = city.City

class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_functions = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func_name, func_obj in self.city_functions:
            self.assertIsNot(func_obj.__doc__, None,
                             "{:s} method needs a docstring".format(func_name))
            self.assertTrue(len(func_obj.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func_name)


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city_instance = City()
        self.assertIsInstance(city_instance, BaseModel)
        self.assertTrue(hasattr(city_instance, "id"))
        self.assertTrue(hasattr(city_instance, "created_at"))
        self.assertTrue(hasattr(city_instance, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "name"))
        if models.storage_t == 'db':
            self.assertEqual(city_instance.name, None)
        else:
            self.assertEqual(city_instance.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(city_instance.state_id, None)
        else:
            self.assertEqual(city_instance.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_dict = c.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city_instance = City()
        new_dict = city_instance.to_dict()
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], city_instance.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], city_instance.updated_at.strftime(time_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city_instance = City()
        string = "[City] ({}) {}".format(city_instance.id, city_instance.__dict__)
        self.assertEqual(string, str(city_instance))

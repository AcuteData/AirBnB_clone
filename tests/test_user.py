#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest

User = user.User

class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_functions = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the User class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func_name, func in self.user_functions:
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(func_name))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func_name))

class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user_instance = User()
        self.assertIsInstance(user_instance, BaseModel)
        self.assertTrue(hasattr(user_instance, "id"))
        self.assertTrue(hasattr(user_instance, "created_at"))
        self.assertTrue(hasattr(user_instance, "updated_at"))

    def test_email_attr(self):
        """Test that User has an attribute 'email', and it's an empty string"""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "email"))
        if models.storage_t == 'db':
            self.assertEqual(user_instance.email, None)
        else:
            self.assertEqual(user_instance.email, "")

    def test_password_attr(self):
        """Test that User has an attribute 'password', and it's an empty string"""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "password"))
        if models.storage_t == 'db':
            self.assertEqual(user_instance.password, None)
        else:
            self.assertEqual(user_instance.password, "")

    def test_first_name_attr(self):
        """Test that User has an attribute 'first_name', and it's an empty string"""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(user_instance.first_name, None)
        else:
            self.assertEqual(user_instance.first_name, "")

    def test_last_name_attr(self):
        """Test that User has an attribute 'last_name', and it's an empty string"""
        user_instance = User()
        self.assertTrue(hasattr(user_instance, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(user_instance.last_name, None)
        else:
            self.assertEqual(user_instance.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attributes"""
        u = User()
        user_dict = u.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertFalse("_sa_instance_state" in user_dict)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in user_dict)
        self.assertTrue("__class__" in user_dict)

    def test_to_dict_values(self):
        """test that values in the dictionary returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        user_dict = u.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual(user_dict["created_at"], u.created_at.strftime(time_format))
        self.assertEqual(user_dict["updated_at"], u.updated_at.strftime(time_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user_instance = User()
        string = "[User] ({}) {}".format(user_instance.id, user_instance.__dict__)
        self.assertEqual(string, str(user_instance))

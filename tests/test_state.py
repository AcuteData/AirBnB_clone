#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
import models
from models import state
from models.base_model import BaseModel
import pep8
import unittest

State = state.State

class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_functions = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(state.__doc__, None, "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1, "state.py needs a docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None, "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1, "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func_name, func in self.state_functions:
            self.assertIsNot(func.__doc__, None, f"{func_name} method needs a docstring")
            self.assertTrue(len(func.__doc__) >= 1, f"{func_name} method needs a docstring")

class TestState(unittest.TestCase):
    """Test the State class"""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state_instance = State()
        self.assertIsInstance(state_instance, BaseModel)
        self.assertTrue(hasattr(state_instance, "id"))
        self.assertTrue(hasattr(state_instance, "created_at"))
        self.assertTrue(hasattr(state_instance, "updated_at"))

    def test_name_attr(self):
        """Test that State has an attribute 'name' and it's an empty string"""
        state_instance = State()
        self.assertTrue(hasattr(state_instance, "name"))
        if models.storage_t == 'db':
            self.assertEqual(state_instance.name, None)
        else:
            self.assertEqual(state_instance.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        state_instance = State()
        state_dict = state_instance.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertFalse("_sa_instance_state" in state_dict)
        for attr in state_instance.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in state_dict)
        self.assertTrue("__class__" in state_dict)

    def test_to_dict_values(self):
        """Test that values in the dictionary returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        state_instance = State()
        state_dict = state_instance.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)
        self.assertEqual(state_dict["created_at"], state_instance.created_at.strftime(time_format))
        self.assertEqual(state_dict["updated_at"], state_instance.updated_at.strftime(time_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        state_instance = State()
        string = "[State] ({}) {}".format(state_instance.id, state_instance.__dict__)
        self.assertEqual(string, str(state_instance))

#!/usr/bin/python3
"""
Contains the TestReviewDocs classes
"""

from datetime import datetime
import inspect
import models
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review

class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_functions = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func_name, func_obj in self.review_functions:
            self.assertIsNot(func_obj.__doc__, None,
                             "{:s} method needs a docstring".format(func_name))
            self.assertTrue(len(func_obj.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func_name)


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review_instance = Review()
        self.assertIsInstance(review_instance, BaseModel)
        self.assertTrue(hasattr(review_instance, "id"))
        self.assertTrue(hasattr(review_instance, "created_at"))
        self.assertTrue(hasattr(review_instance, "updated_at"))

    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(review_instance.place_id, None)
        else:
            self.assertEqual(review_instance.place_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review_instance.user_id, None)
        else:
            self.assertEqual(review_instance.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review_instance.text, None)
        else:
            self.assertEqual(review_instance.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_dict = r.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dict)
        self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_dict = r.to_dict()
        self.assertEqual(new_dict["__class__"], "Review")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], r.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], r.updated_at.strftime(time_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review_instance = Review()
        string = "[Review] ({}) {}".format(review_instance.id, review_instance.__dict__)
        self.assertEqual(string, str(review_instance))

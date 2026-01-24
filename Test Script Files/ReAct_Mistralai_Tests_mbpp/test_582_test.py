import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):

    def test_empty_dict(self):
        """Test if an empty dictionary returns True"""
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        """Test if a non-empty dictionary returns False"""
        self.assertFalse(my_dict({"key": "value"}))

    def test_none_type(self):
        """Test if None type returns True"""
        self.assertTrue(my_dict(None))

    def test_list_type(self):
        """Test if list type raises a TypeError"""
        with self.assertRaises(TypeError):
            my_dict([1, 2, 3])

    def test_set_type(self):
        """Test if set type raises a TypeError"""
        with self.assertRaises(TypeError):
            my_dict({1, 2, 3})

    def test_string_type(self):
        """Test if string type raises a TypeError"""
        with self.assertRaises(TypeError):
            my_dict("string")

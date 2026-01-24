import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({"key": "value"}))

    def test_none_input(self):
        self.assertTrue(my_dict(None))

    def test_empty_list(self):
        self.assertTrue(my_dict([]))

    def test_list_with_elements(self):
        self.assertFalse(my_dict([1, 2, 3]))

    def test_zero(self):
        self.assertTrue(my_dict(0))

    def test_negative_number(self):
        self.assertTrue(my_dict(-1))

    def test_string(self):
        self.assertTrue(my_dict(""))

    def test_non_string(self):
        self.assertTrue(my_dict(123))

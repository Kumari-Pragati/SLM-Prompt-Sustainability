import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):

    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({'key': 'value'}))

    def test_none_input(self):
        self.assertTrue(my_dict(None))

    def test_integer_input(self):
        self.assertTrue(my_dict(123))

    def test_float_input(self):
        self.assertTrue(my_dict(123.45))

    def test_string_input(self):
        self.assertTrue(my_dict('string'))

    def test_list_input(self):
        self.assertTrue(my_dict([]))

    def test_tuple_input(self):
        self.assertTrue(my_dict(()))

import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(my_dict({1: 2, 3: 4}))

    def test_simple_false(self):
        self.assertFalse(my_dict({}))

    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_single_key_dict(self):
        self.assertFalse(my_dict({1: 2}))

    def test_single_value_dict(self):
        self.assertFalse(my_dict({1: 1}))

    def test_negative_key_dict(self):
        self.assertFalse(my_dict({-1: 2}))

    def test_float_key_dict(self):
        self.assertFalse(my_dict({3.14: 2}))

    def test_list_value_dict(self):
        self.assertFalse(my_dict({1: [1, 2, 3]}))

    def test_tuple_value_dict(self):
        self.assertFalse(my_dict({1: (1, 2, 3)}))

    def test_string_value_dict(self):
        self.assertFalse(my_dict({1: 'test'}))

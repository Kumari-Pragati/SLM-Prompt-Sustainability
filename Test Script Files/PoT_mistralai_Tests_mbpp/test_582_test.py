import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({'key': 'value'}))

    def test_none_type(self):
        self.assertTrue(my_dict(None))

    def test_list_type(self):
        self.assertFalse(my_dict([1, 2, 3]))

    def test_set_type(self):
        self.assertFalse(my_dict({1, 2, 3}))

    def test_tuple_type(self):
        self.assertFalse(my_dict((1, 2, 3)))

    def test_str_type(self):
        self.assertFalse(my_dict('string'))

    def test_int_type(self):
        self.assertTrue(my_dict(0))

import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({'a': 1}))

    def test_none_input(self):
        self.assertTrue(my_dict(None))

    def test_empty_list(self):
        self.assertTrue(my_dict([]))

    def test_empty_tuple(self):
        self.assertTrue(my_dict(()))

    def test_empty_string(self):
        self.assertTrue(my_dict(''))

    def test_empty_set(self):
        self.assertTrue(my_dict(set()))

import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):

    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dict(self):
        self.assertFalse(my_dict({'a': 1}))

    def test_dict_with_no_keys(self):
        self.assertTrue(my_dict({}))

    def test_dict_with_keys(self):
        self.assertFalse(my_dict({'a': 1, 'b': 2}))

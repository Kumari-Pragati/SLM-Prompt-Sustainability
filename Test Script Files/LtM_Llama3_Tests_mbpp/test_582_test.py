import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_true(self):
        self.assertTrue(my_dict({}))

    def test_false(self):
        self.assertFalse(my_dict({'a': 1}))

    def test_empty_dict(self):
        self.assertTrue(my_dict({}))

    def test_non_dict(self):
        with self.assertRaises(TypeError):
            my_dict('')

    def test_dict_with_non_dict_value(self):
        with self.assertRaises(TypeError):
            my_dict({'a': 'b', 'c': 1})

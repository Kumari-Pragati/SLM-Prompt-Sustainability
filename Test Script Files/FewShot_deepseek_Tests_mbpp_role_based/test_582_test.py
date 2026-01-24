import unittest
from mbpp_582_code import my_dict

class TestMyDict(unittest.TestCase):
    def test_empty_dictionary(self):
        self.assertTrue(my_dict({}))

    def test_non_empty_dictionary(self):
        self.assertFalse(my_dict({'key': 'value'}))

    def test_none_input(self):
        with self.assertRaises(TypeError):
            my_dict(None)

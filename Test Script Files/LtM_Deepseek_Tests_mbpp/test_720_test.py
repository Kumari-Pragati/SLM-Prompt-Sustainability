import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b'), {'c': 'd'}), (('a', 'b'), {'c': 'd'}))

    def test_empty_input(self):
        self.assertEqual(add_dict_to_tuple((), {}), ((), {}))

    def test_dict_as_last_element(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b'), {'c': 'd'}), (('a', 'b'), {'c': 'd'}))

    def test_large_dict(self):
        large_dict = {i: i for i in range(1000)}
        self.assertEqual(add_dict_to_tuple(('a', 'b'), large_dict), (('a', 'b'), large_dict))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_dict_to_tuple('a', {'c': 'd'})

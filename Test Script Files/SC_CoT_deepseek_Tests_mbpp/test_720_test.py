import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b', 'c'), {'d': 'e'}), (('a', 'b', 'c', {'d': 'e'})))

    def test_empty_tuple(self):
        self.assertEqual(add_dict_to_tuple((), {'d': 'e'}), (({'d': 'e'},)))

    def test_empty_dict(self):
        self.assertEqual(add_dict_to_tuple(('a', 'b', 'c'), {}), (('a', 'b', 'c', {})))

    def test_single_element_tuple(self):
        self.assertEqual(add_dict_to_tuple(('a',), {'d': 'e'}), (('a', {'d': 'e'})))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            add_dict_to_tuple('a', {'d': 'e'})

        with self.assertRaises(TypeError):
            add_dict_to_tuple(('a', 'b', 'c'), 'd')

        with self.assertRaises(TypeError):
            add_dict_to_tuple(123, {'d': 'e'})

        with self.assertRaises(TypeError):
            add_dict_to_tuple(('a', 'b', 'c'), 123)

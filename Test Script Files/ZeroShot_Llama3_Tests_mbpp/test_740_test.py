import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_dict(()), {})

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_dict(('a',)), {'a': None})

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_dict(('a', 'b', 'c', 'd')), {'a': 'b', 'c': 'd'})

    def test_tuple_with_non_string_values(self):
        self.assertEqual(tuple_to_dict((1, 2, 3, 4)), {1: 2, 3: 4})

    def test_tuple_with_non_integer_indices(self):
        with self.assertRaises(TypeError):
            tuple_to_dict((1, 2, 3, 4, 5))

    def test_tuple_with_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_dict('abc')

    def test_tuple_with_non_tuple_input_type(self):
        with self.assertRaises(TypeError):
            tuple_to_dict([1, 2, 3, 4])

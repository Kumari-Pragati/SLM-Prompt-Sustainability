import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_single_element_list(self):
        self.assertEqual(flatten_tuple([1]), '1')

    def test_single_element_tuple(self):
        self.assertEqual(flatten_tuple([(1,)]), '1')

    def test_multiple_elements_list(self):
        self.assertEqual(flatten_tuple([1, 2, 3]), '1 2 3')

    def test_multiple_elements_tuple(self):
        self.assertEqual(flatten_tuple([(1,), (2,), (3,)]), '1 2 3')

    def test_mixed_list_and_tuple(self):
        self.assertEqual(flatten_tuple([1, (2,), 3]), '1 2 3')

    def test_nested_tuples(self):
        self.assertEqual(flatten_tuple([(1, (2, 3)), (4, 5)]), '1 2 3 4 5')

    def test_empty_tuple(self):
        self.assertEqual(flatten_tuple(()), '')

    def test_invalid_input(self):
        self.assertRaises(TypeError, flatten_tuple, 'string')

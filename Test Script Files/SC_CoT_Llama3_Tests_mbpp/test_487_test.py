import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sort_tuple(('a', 'c', 'b')), ('a', 'b', 'c'))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(sort_tuple(('a',)), ('a',))

    def test_edge_case_two_elements_tuple(self):
        self.assertEqual(sort_tuple(('a', 'b')), ('a', 'b'))

    def test_edge_case_descending_order(self):
        self.assertEqual(sort_tuple(('b', 'a')), ('a', 'b'))

    def test_edge_case_ascending_order(self):
        self.assertEqual(sort_tuple(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            sort_tuple('a')

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            sort_tuple(123)

    def test_invalid_input_non_string_elements(self):
        with self.assertRaises(TypeError):
            sort_tuple((123, 456, 789))

    def test_invalid_input_non_hashable_elements(self):
        with self.assertRaises(TypeError):
            sort_tuple([1, 2, 3])

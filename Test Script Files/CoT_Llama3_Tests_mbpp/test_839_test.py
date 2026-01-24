import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(sort_tuple((1,)), (1,))

    def test_sorted_tuple(self):
        self.assertEqual(sort_tuple((1, 2, 3)), (1, 2, 3))

    def test_unsorted_tuple(self):
        self.assertEqual(sort_tuple((3, 1, 2)), (1, 2, 3))

    def test_tuple_with_duplicates(self):
        self.assertEqual(sort_tuple((1, 2, 2, 3)), (1, 2, 2, 3))

    def test_tuple_with_negative_numbers(self):
        self.assertEqual(sort_tuple((-1, 0, 1)), (-1, 0, 1))

    def test_tuple_with_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_tuple((1, 'a', 2))

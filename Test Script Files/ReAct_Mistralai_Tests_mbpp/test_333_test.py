import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(Sort([(1, 1)]), [(1, 1)])

    def test_sort_multiple_elements_same_key(self):
        self.assertEqual(Sort([(1, 2), (1, 3), (1, 4)]), [(1, 2), (1, 3), (1, 4)])

    def test_sort_multiple_elements_different_keys(self):
        self.assertEqual(Sort([(2, 1), (1, 2), (3, 1)]), [(1, 2), (2, 1), (3, 1)])

    def test_sort_negative_numbers(self):
        self.assertEqual(Sort([(-2, 1), (-1, 2), (0, 3), (1, 4)]), [(-2, 1), (-1, 2), (0, 3), (1, 4)])

    def test_sort_mixed_types(self):
        with self.assertRaises(TypeError):
            Sort([(1, 'a'), (2, 3), (4, 'b')])

    def test_sort_duplicate_keys(self):
        self.assertEqual(Sort([(1, 1), (1, 2)]), [(1, 1), (1, 2)])

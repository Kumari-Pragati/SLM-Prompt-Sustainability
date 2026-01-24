import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_tuples([], 2), '[]')

    def test_single_element(self):
        self.assertEqual(find_tuples([1], 1), '[]')
        self.assertEqual(find_tuples([2], 2), '[[2]]')
        self.assertEqual(find_tuples([3], 2), '[]')

    def test_multiple_elements(self):
        self.assertEqual(find_tuples([0, 4, 8, 12], 4), '[[0, 4, 8, 12]]')
        self.assertEqual(find_tuples([1, 3, 5, 7], 4), '[]')
        self.assertEqual(find_tuples([2, 6, 10, 14], 2), '[[2, 6, 10, 14]]')

    def test_negative_numbers(self):
        self.assertEqual(find_tuples([-2, -4, -6, -8], 2), '[[2, 4, 6, 8]]')

    def test_floats(self):
        self.assertEqual(find_tuples([0.0, 4.0, 8.0, 12.0], 4), '[[0.0, 4.0, 8.0, 12.0]]')

    def test_mixed_types(self):
        self.assertEqual(find_tuples([1, 2, 'three', 4], 2), '[[1, 2], []]')

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_tuples, [1, 2, 3], 'invalid')
        self.assertRaises(TypeError, find_tuples, [1, 2, 3], 0.5)
        self.assertRaises(TypeError, find_tuples, [1, 2, 3], (1, 2, 3))

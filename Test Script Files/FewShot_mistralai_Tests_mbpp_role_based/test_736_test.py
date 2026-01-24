import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(left_insertion([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(left_insertion([1], 0), 0)
        self.assertEqual(left_insertion([1], 1), 1)

    def test_positive_numbers(self):
        self.assertEqual(left_insertion([1, 2, 3, 4], 0), 0)
        self.assertEqual(left_insertion([1, 2, 3, 4], 1), 1)
        self.assertEqual(left_insertion([1, 2, 3, 4], 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-1, -2, -3, -4], 0), 0)
        self.assertEqual(left_insertion([-1, -2, -3, -4], -1), 0)
        self.assertEqual(left_insertion([-1, -2, -3, -4], -4), 4)

    def test_zero(self):
        self.assertEqual(left_insertion([0], 0), 0)
        self.assertEqual(left_insertion([0], 1), 1)

    def test_duplicates(self):
        self.assertEqual(left_insertion([1, 1, 2, 3], 1), 1)
        self.assertEqual(left_insertion([1, 1, 2, 3], 2), 2)
        self.assertEqual(left_insertion([1, 1, 2, 3], 3), 3)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, left_insertion, [1, 2, 3], 'a')
        self.assertRaises(TypeError, left_insertion, [], 'a')

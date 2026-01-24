import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 3), 0)

    def test_single_element(self):
        self.assertEqual(left_insertion([1], 3), 1)
        self.assertEqual(left_insertion([-1], 3), 0)

    def test_multiple_elements(self):
        self.assertEqual(left_insertion([1, 2, 3, 4], 1), 0)
        self.assertEqual(left_insertion([1, 2, 3, 4], 2), 1)
        self.assertEqual(left_insertion([1, 2, 3, 4], 5), 4)
        self.assertEqual(left_insertion([5, 4, 3, 2, 1], 5), 0)
        self.assertEqual(left_insertion([5, 4, 3, 2, 1], 1), 4)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-1, -2, -3], -1), 0)
        self.assertEqual(left_insertion([-1, -2, -3], -2), 1)
        self.assertEqual(left_insertion([-1, -2, -3], -4), 3)

    def test_duplicates(self):
        self.assertEqual(left_insertion([1, 1, 2, 2, 3], 1), 0)
        self.assertEqual(left_insertion([1, 1, 2, 2, 3], 2), 2)
        self.assertEqual(left_insertion([1, 1, 2, 2, 3], 3), 4)

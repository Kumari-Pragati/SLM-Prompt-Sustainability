import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_single_number(self):
        self.assertIsNone(second_smallest([5]))

    def test_two_same_numbers(self):
        self.assertIsNone(second_smallest([5, 5]))

    def test_two_different_numbers(self):
        self.assertEqual(second_smallest([5, 3]), 3)

    def test_sorted_list(self):
        self.assertEqual(second_smallest([3, 5, 7]), 5)

    def test_unsorted_list(self):
        self.assertEqual(second_smallest([7, 5, 3]), 5)

    def test_large_list(self):
        self.assertEqual(second_smallest(list(range(1, 1001)) + [5]), 6)

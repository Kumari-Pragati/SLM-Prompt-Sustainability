import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(second_smallest([7, 1, 3, 2, 4, 8, 6]), 2)

    def test_single_element(self):
        self.assertIsNone(second_smallest([5]))

    def def test_duplicate_elements(self):
        self.assertEqual(second_smallest([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-7, -1, -3, -2, -4, -8, -6]), -2)

    def test_zero(self):
        self.assertEqual(second_smallest([0, 1, 2, 3, 4]), 0)

    def test_large_numbers(self):
        self.assertEqual(second_smallest(list(range(10000, 0, -1))), 9999)

    def test_duplicate_and_negative_numbers(self):
        self.assertEqual(second_smallest([-7, -1, -3, -2, -4, -8, -6, -2]), -2)

    def test_duplicate_and_large_numbers(self):
        self.assertEqual(second_smallest([1000000, 999999, 1000000]), 999999)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([1, 2, 3, 4]), 2)

    def test_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_duplicate_elements(self):
        self.assertEqual(second_smallest([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-1, -2, -3, -4]), -2)

    def test_duplicate_negative_numbers(self):
        self.assertEqual(second_smallest([-2, -2, -2, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(second_smallest([-1, 0, 1, 2]), 0)

    def test_duplicate_mixed_numbers(self):
        self.assertEqual(second_smallest([0, 0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_two_same_elements(self):
        self.assertIsNone(second_smallest([2, 2]))

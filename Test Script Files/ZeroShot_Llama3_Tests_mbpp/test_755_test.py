import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_single_element_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_element_list(self):
        self.assertEqual(second_smallest([1, 1]), None)

    def test_three_element_list(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_four_element_list(self):
        self.assertEqual(second_smallest([1, 2, 3, 4]), 2)

    def test_five_element_list(self):
        self.assertEqual(second_smallest([1, 1, 2, 3, 4]), 2)

    def test_duplicates(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 4]), 2)

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-1, -2, -3, -4]), -2)

    def test_positive_numbers(self):
        self.assertEqual(second_smallest([1, 2, 3, 4]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(second_smallest([1, -2, 3, 4]), 1)

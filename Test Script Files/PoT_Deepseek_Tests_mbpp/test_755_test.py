import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([3, 1, 2]), 2)

    def test_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_duplicate_elements(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-3, -1, -2]), -2)

    def test_large_numbers(self):
        self.assertEqual(second_smallest([1000, 2000, 500]), 500)

    def test_mixed_numbers(self):
        self.assertEqual(second_smallest([3, -1, 2]), 2)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

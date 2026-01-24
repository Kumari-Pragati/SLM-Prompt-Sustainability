import unittest

from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)

    def test_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_duplicate_elements(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-5, -3, -1, 0, 1]), -1)

    def test_duplicate_negative_numbers(self):
        self.assertIsNone(second_smallest([-1, -1]))

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_large_numbers(self):
        self.assertEqual(second_smallest(list(range(1, 10001))), 2)

    def test_duplicate_large_numbers(self):
        self.assertIsNone(second_smallest([10000, 10000]))

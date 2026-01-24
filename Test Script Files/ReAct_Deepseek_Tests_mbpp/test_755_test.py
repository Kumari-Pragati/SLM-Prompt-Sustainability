import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([5, 3, 2, 1, 4]), 3)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(second_smallest([5, 5, 3, 2, 1, 1]), 2)

    def test_single_element(self):
        self.assertIsNone(second_smallest([5]))

    def test_two_elements_same(self):
        self.assertIsNone(second_smallest([5, 5]))

    def test_two_elements_different(self):
        self.assertEqual(second_smallest([5, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_large_numbers(self):
        self.assertEqual(second_smallest(list(range(1000, 0, -1))), 999)

    def test_negative_numbers(self):
        self.assertEqual(second_smallest([-5, -3, -2, -1]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(second_smallest([-5, 3, 0, -1, 2]), 0)

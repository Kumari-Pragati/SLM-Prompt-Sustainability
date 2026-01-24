import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_elements(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_three_elements(self):
        self.assertEqual(second_smallest([1, 2, 2]), 2)

    def test_duplicates(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 4, 4]), 2)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_list_with_one_unique_element(self):
        self.assertEqual(second_smallest([1, 1, 1, 1, 1]), None)

    def test_list_with_all_duplicates(self):
        self.assertIsNone(second_smallest([1, 1, 1, 1, 1, 1]))

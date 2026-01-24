import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_single_element_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_equal_elements_list(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_single_unique_element_list(self):
        self.assertEqual(second_smallest([1]), 1)

    def test_two_unique_elements_list(self):
        self.assertEqual(second_smallest([1, 2]), 1)

    def test_three_unique_elements_list(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_duplicate_elements_list(self):
        self.assertEqual(second_smallest([1, 1, 2, 3]), 1)

    def test_large_list_with_duplicates(self):
        self.assertEqual(second_smallest([1, 2, 1, 3, 2, 1, 4, 2]), 3)

import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_single_element_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_equal_elements(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_two_distinct_elements(self):
        self.assertEqual(second_smallest([1, 2]), 2)

    def test_three_distinct_elements(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_list_with_duplicates(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3]), 2)

    def test_list_with_duplicates_and_empty(self):
        self.assertIsNone(second_smallest([1, 1, 2, 2, 3, 3]))

    def test_list_with_duplicates_and_empty_and_single(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4]), 3)

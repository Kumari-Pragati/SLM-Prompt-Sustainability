import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_single_element_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_list_with_duplicates(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 4, 4]), 2)

    def test_list_with_duplicates_and_duplicates_at_start(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3]), 2)

    def test_list_with_duplicates_and_duplicates_at_end(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 4, 4, 4]), 2)

    def test_list_with_duplicates_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 3, 4, 4, 5]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_end(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 2)

    def test_list_with_duplicates_and_duplicates_at_start_and_end_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 5, 6]), 3)

    def test_list_with_duplicates_and_duplicates_at_end_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 3, 4, 4, 5, 5, 6]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_start(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_end(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_start_and_duplicates_at_end(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]), 3)

    def test_list_with_duplicates_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_start_and_duplicates_at_end_and_duplicates_in_middle_and_duplicates_at_start(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
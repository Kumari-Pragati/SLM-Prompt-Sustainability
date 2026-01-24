import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)

    def test_edge_case_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_edge_case_two_elements(self):
        self.assertEqual(second_smallest([1, 1]), None)

    def test_edge_case_two_distinct_elements(self):
        self.assertEqual(second_smallest([1, 2]), 1)

    def test_edge_case_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3]), 1)

    def test_edge_case_list_with_duplicates_and_empty(self):
        self.assertIsNone(second_smallest([1, 1, 2, 2, 3, 3]))

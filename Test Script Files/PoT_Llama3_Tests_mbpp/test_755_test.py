import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([2, 3, 4, 5, 6]), 4)

    def test_edge_case_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_edge_case_two_elements(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_edge_case_two_elements_equal(self):
        self.assertIsNone(second_smallest([1, 2]))

    def test_edge_case_empty_list(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_single_element_list(self):
        self.assertIsNone(second_smallest([1]))

    def test_edge_case_duplicates(self):
        self.assertEqual(second_smallest([1, 2, 2, 3, 4, 5]), 2)

    def test_edge_case_duplicates_sorted(self):
        self.assertEqual(second_smallest([1, 1, 2, 2, 3, 3]), 2)

    def test_edge_case_duplicates_sorted_descending(self):
        self.assertEqual(second_smallest([5, 5, 4, 4, 3, 3]), 4)

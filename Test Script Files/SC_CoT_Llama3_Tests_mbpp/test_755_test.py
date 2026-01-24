import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)

    def test_edge_case_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_edge_case_single_element_duplicates(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_edge_case_single_element_empty(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_two_elements(self):
        self.assertEqual(second_smallest([1, 1]), None)

    def test_edge_case_two_elements_duplicates(self):
        self.assertEqual(second_smallest([1, 1]), None)

    def test_edge_case_two_elements_empty(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_three_elements(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_edge_case_three_elements_duplicates(self):
        self.assertEqual(second_smallest([1, 1, 2]), 1)

    def test_edge_case_three_elements_empty(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_three_elements_empty_duplicates(self):
        self.assertIsNone(second_smallest([1, 1, 1]))

    def test_edge_case_three_elements_empty_duplicates(self):
        self.assertIsNone(second_smallest([]))

    def test_edge_case_three_elements_empty_duplicates(self):
        self.assertIsNone(second_smallest([]))

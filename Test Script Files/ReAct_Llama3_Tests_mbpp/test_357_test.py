import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6]]), 6)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(find_max([[10]]), 10)

    def test_edge_case_single_element_list_with_negative(self):
        self.assertEqual(find_max([[-10]]), -10)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_edge_case_list_with_negative_and_positive(self):
        self.assertEqual(find_max([[-1, 2, 3], [4, 5, -6]]), 5)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(find_max([[1, 2, 2], [3, 4, 5]]), 5)

    def test_edge_case_list_with_negative_duplicates(self):
        self.assertEqual(find_max([[-1, -2, -2], [-3, -4, -5]]), -1)

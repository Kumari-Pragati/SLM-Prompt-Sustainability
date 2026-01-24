import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(two_unique_nums([1]), [])

    def test_edge_case_all_duplicates_list(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1, 1]), [])

    def test_edge_case_all_unique_list(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_two_unique_nums(self):
        self.assertEqual(two_unique_nums([1, 2, 2, 3, 3, 4, 5, 5]), [1, 4])

    def test_edge_case_multiple_unique_nums(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_duplicates_and_unique(self):
        self.assertEqual(two_unique_nums([1, 1, 2, 2, 3, 3, 4, 5, 5]), [1, 4])

    def test_edge_case_duplicates_and_unique_reverse(self):
        self.assertEqual(two_unique_nums([5, 5, 4, 3, 3, 2, 2, 1, 1]), [4, 1])

import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 4])

    def test_edge_case_single_element(self):
        self.assertEqual(two_unique_nums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_edge_case_single_unique_element(self):
        self.assertEqual(two_unique_nums([1, 1]), [1])

    def test_edge_case_all_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1]), [])

    def test_edge_case_all_unique(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_edge_case_all_duplicates_and_one_unique(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 2]), [2])

import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])
        self.assertListEqual(two_unique_nums([4, 4, 5, 6]), [5, 6])

    def test_edge_case_empty_list(self):
        self.assertListEqual(two_unique_nums([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(two_unique_nums([1]), [])

    def test_edge_case_duplicates(self):
        self.assertListEqual(two_unique_nums([1, 1]), [])
        self.assertListEqual(two_unique_nums([1, 1, 2]), [2])

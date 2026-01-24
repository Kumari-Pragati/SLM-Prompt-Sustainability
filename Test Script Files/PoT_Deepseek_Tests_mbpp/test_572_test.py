import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])

    def test_edge_case_single_element(self):
        self.assertEqual(two_unique_nums([1]), [1])

    def test_boundary_case_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_corner_case_all_elements_unique(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_corner_case_all_elements_same(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1, 1]), [])

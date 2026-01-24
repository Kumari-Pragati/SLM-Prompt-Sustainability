import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_edge_case_min(self):
        self.assertTrue(check_Consecutive([0, 1, 2]))

    def test_edge_case_max(self):
        self.assertTrue(check_Consecutive([5, 6, 7]))

    def test_edge_case_single_element(self):
        self.assertTrue(check_Consecutive([1]))

    def test_boundary_case_empty_list(self):
        self.assertTrue(check_Consecutive([]))

    def test_corner_case_decreasing(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1]))

    def test_corner_case_duplicates(self):
        self.assertTrue(check_Consecutive([1, 1, 2, 3]))

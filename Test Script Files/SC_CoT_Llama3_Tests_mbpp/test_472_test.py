import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_Consecutive([]))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_Consecutive([1]))

    def test_edge_case_single_element_list_reverse(self):
        self.assertTrue(check_Consecutive([5, 4, 3, 2, 1]))

    def test_edge_case_max_min_equal(self):
        self.assertTrue(check_Consecutive([1, 1]))

    def test_edge_case_max_min_equal_reverse(self):
        self.assertTrue(check_Consecutive([1, 2, 1]))

    def test_edge_case_max_min_not_equal(self):
        self.assertFalse(check_Consecutive([1, 2, 3]))

    def test_edge_case_max_min_not_equal_reverse(self):
        self.assertFalse(check_Consecutive([5, 4, 3]))

    def test_edge_case_max_min_not_equal_reverse2(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1]))

    def test_edge_case_max_min_not_equal_reverse3(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0]))

    def test_edge_case_max_min_not_equal_reverse4(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0, -1]))

    def test_edge_case_max_min_not_equal_reverse5(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0, -1, -2]))

    def test_edge_case_max_min_not_equal_reverse6(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0, -1, -2, -3]))

    def test_edge_case_max_min_not_equal_reverse7(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0, -1, -2, -3, -4]))

    def test_edge_case_max_min_not_equal_reverse8(self):
        self.assertFalse(check_Consecutive([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]))

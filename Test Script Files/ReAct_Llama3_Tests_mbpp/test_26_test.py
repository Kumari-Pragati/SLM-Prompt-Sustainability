import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 1))

    def test_edge_case1(self):
        self.assertFalse(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 4)], 1))

    def test_edge_case2(self):
        self.assertFalse(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 4))

    def test_edge_case3(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 3))

    def test_edge_case4(self):
        self.assertFalse(check_k_elements([], 1))

    def test_edge_case5(self):
        self.assertTrue(check_k_elements([(1, 1, 1)], 1))

    def test_edge_case6(self):
        self.assertFalse(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)], 5))

    def test_edge_case7(self):
        self.assertFalse(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)], 1))

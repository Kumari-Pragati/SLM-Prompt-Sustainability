import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 10)

    def test_edge_case2(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case3(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case4(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_edge_case5(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_edge_case6(self):
        self.assertEqual(get_inv_count([1, 2], 2), 1)

    def test_edge_case7(self):
        self.assertEqual(get_inv_count([1, 2, 3], 3), 3)

    def test_edge_case8(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5, 6], 6), 15)

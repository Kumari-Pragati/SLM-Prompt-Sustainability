import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)

    def test_edge_case3(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 0), 1)

    def test_edge_case4(self):
        self.assertEqual(find_Sum([], 0), None)

    def test_edge_case5(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 6), None)

    def test_edge_case6(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], -1), None)

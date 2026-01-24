import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 3, 4], 3), 4)

    def test_edge_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 2, 1], 3), 4)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 3, 2], 3), 4)

    def test_edge_case4(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 1, 3], 3), 4)

    def test_edge_case5(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 1, 2], 3), 4)

    def test_edge_case6(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 3, 1], 3), 4)

    def test_edge_case7(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 2, 1], 3), 4)

    def test_edge_case8(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 3, 2], 3), 4)

    def test_edge_case9(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 1, 3], 3), 4)

    def test_edge_case10(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [3, 1, 2], 3), 4)

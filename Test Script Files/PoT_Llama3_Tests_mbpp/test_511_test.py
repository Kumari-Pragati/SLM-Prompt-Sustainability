import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum(12), 7)

    def test_edge_case(self):
        self.assertEqual(find_Min_Sum(1), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Sum(2), 2)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Sum(3), 4)

    def test_edge_case4(self):
        self.assertEqual(find_Min_Sum(4), 4)

    def test_edge_case5(self):
        self.assertEqual(find_Min_Sum(5), 5)

    def test_edge_case6(self):
        self.assertEqual(find_Min_Sum(6), 6)

    def test_edge_case7(self):
        self.assertEqual(find_Min_Sum(7), 8)

    def test_edge_case8(self):
        self.assertEqual(find_Min_Sum(8), 8)

    def test_edge_case9(self):
        self.assertEqual(find_Min_Sum(9), 9)

    def test_edge_case10(self):
        self.assertEqual(find_Min_Sum(10), 10)

    def test_edge_case11(self):
        self.assertEqual(find_Min_Sum(11), 11)

    def test_edge_case12(self):
        self.assertEqual(find_Min_Sum(12), 7)

    def test_edge_case13(self):
        self.assertEqual(find_Min_Sum(13), 7)

    def test_edge_case14(self):
        self.assertEqual(find_Min_Sum(14), 7)

    def test_edge_case15(self):
        self.assertEqual(find_Min_Sum(15), 7)

    def test_edge_case16(self):
        self.assertEqual(find_Min_Sum(16), 8)

    def test_edge_case17(self):
        self.assertEqual(find_Min_Sum(17), 8)

    def test_edge_case18(self):
        self.assertEqual(find_Min_Sum(18), 8)

    def test_edge_case19(self):
        self.assertEqual(find_Min_Sum(19), 8)

    def test_edge_case20(self):
        self.assertEqual(find_Min_Sum(20), 8)

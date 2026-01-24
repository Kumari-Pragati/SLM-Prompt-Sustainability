import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Min_Squares(12), 3)

    def test_edge_case(self):
        self.assertEqual(get_Min_Squares(3), 3)

    def test_edge_case2(self):
        self.assertEqual(get_Min_Squares(4), 1)

    def test_edge_case3(self):
        self.assertEqual(get_Min_Squares(1), 1)

    def test_edge_case4(self):
        self.assertEqual(get_Min_Squares(2), 1)

    def test_edge_case5(self):
        self.assertEqual(get_Min_Squares(0), 0)

    def test_edge_case6(self):
        self.assertEqual(get_Min_Squares(3), 3)

    def test_edge_case7(self):
        self.assertEqual(get_Min_Squares(4), 2)

    def test_edge_case8(self):
        self.assertEqual(get_Min_Squares(9), 3)

    def test_edge_case9(self):
        self.assertEqual(get_Min_Squares(16), 4)

    def test_edge_case10(self):
        self.assertEqual(get_Min_Squares(20), 4)

    def test_edge_case11(self):
        self.assertEqual(get_Min_Squares(25), 5)

    def test_edge_case12(self):
        self.assertEqual(get_Min_Squares(36), 6)

    def test_edge_case13(self):
        self.assertEqual(get_Min_Squares(49), 7)

    def test_edge_case14(self):
        self.assertEqual(get_Min_Squares(64), 8)

    def test_edge_case15(self):
        self.assertEqual(get_Min_Squares(81), 9)

    def test_edge_case16(self):
        self.assertEqual(get_Min_Squares(100), 10)

import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])

    def test_edge_case(self):
        self.assertEqual(lucky_num(0), [])

    def test_edge_case2(self):
        self.assertEqual(lucky_num(1), [0])

    def test_edge_case3(self):
        self.assertEqual(lucky_num(2), [0, 2])

    def test_edge_case4(self):
        self.assertEqual(lucky_num(3), [0, 2, 4])

    def test_edge_case5(self):
        self.assertEqual(lucky_num(4), [0, 2, 4, 6])

    def test_edge_case6(self):
        self.assertEqual(lucky_num(5), [0, 2, 4, 6, 8])

    def test_edge_case7(self):
        self.assertEqual(lucky_num(6), [0, 2, 4, 6, 8, 10])

    def test_edge_case8(self):
        self.assertEqual(lucky_num(7), [0, 2, 4, 6, 8, 10, 12])

    def test_edge_case9(self):
        self.assertEqual(lucky_num(8), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_edge_case10(self):
        self.assertEqual(lucky_num(9), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_edge_case11(self):
        self.assertEqual(lucky_num(10), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_edge_case12(self):
        self.assertEqual(lucky_num(11), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_edge_case13(self):
        self.assertEqual(lucky_num(12), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_edge_case14(self):
        self.assertEqual(lucky_num(13), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_edge_case15(self):
        self.assertEqual(lucky_num(14), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_edge_case16(self):
        self.assertEqual(lucky_num(15), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_edge_case17(self):
        self.assertEqual(lucky_num(16), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_edge_case18(self):
        self.assertEqual(lucky_num(17), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_edge_case19(self):
        self.assertEqual(lucky_num(18), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_edge_case20(self):
        self.assertEqual(lucky_num(19), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_edge_case21(self):
        self.assertEqual(lucky_num(20), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
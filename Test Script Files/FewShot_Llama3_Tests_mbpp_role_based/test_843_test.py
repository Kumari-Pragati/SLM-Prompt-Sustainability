import unittest
from mbpp_843_code import nth_super_ugly_number

class TestNthSuperUglyNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 12)

    def test_edge_case_n_1(self):
        self.assertEqual(nth_super_ugly_number(1, [2, 7, 13, 19]), 1)

    def test_edge_case_n_2(self):
        self.assertEqual(nth_super_ugly_number(2, [2, 7, 13, 19]), 2)

    def test_edge_case_n_3(self):
        self.assertEqual(nth_super_ugly_number(3, [2, 7, 13, 19]), 4)

    def test_edge_case_n_4(self):
        self.assertEqual(nth_super_ugly_number(4, [2, 7, 13, 19]), 6)

    def test_edge_case_n_5(self):
        self.assertEqual(nth_super_ugly_number(5, [2, 7, 13, 19]), 8)

    def test_edge_case_n_6(self):
        self.assertEqual(nth_super_ugly_number(6, [2, 7, 13, 19]), 10)

    def test_edge_case_n_7(self):
        self.assertEqual(nth_super_ugly_number(7, [2, 7, 13, 19]), 12)

    def test_edge_case_n_8(self):
        self.assertEqual(nth_super_ugly_number(8, [2, 7, 13, 19]), 14)

    def test_edge_case_n_9(self):
        self.assertEqual(nth_super_ugly_number(9, [2, 7, 13, 19]), 16)

    def test_edge_case_n_10(self):
        self.assertEqual(nth_super_ugly_number(10, [2, 7, 13, 19]), 18)

    def test_edge_case_n_11(self):
        self.assertEqual(nth_super_ugly_number(11, [2, 7, 13, 19]), 20)

    def test_edge_case_n_12(self):
        self.assertEqual(nth_super_ugly_number(12, [2, 7, 13, 19]), 22)

    def test_edge_case_n_13(self):
        self.assertEqual(nth_super_ugly_number(13, [2, 7, 13, 19]), 24)

    def test_edge_case_n_14(self):
        self.assertEqual(nth_super_ugly_number(14, [2, 7, 13, 19]), 26)

    def test_edge_case_n_15(self):
        self.assertEqual(nth_super_ugly_number(15, [2, 7, 13, 19]), 28)

    def test_edge_case_n_16(self):
        self.assertEqual(nth_super_ugly_number(16, [2, 7, 13, 19]), 30)

    def test_edge_case_n_17(self):
        self.assertEqual(nth_super_ugly_number(17, [2, 7, 13, 19]), 32)

    def test_edge_case_n_18(self):
        self.assertEqual(nth_super_ugly_number(18, [2, 7, 13, 19]), 34)

    def test_edge_case_n_19(self):
        self.assertEqual(nth_super_ugly_number(19, [2, 7, 13, 19]), 36)

    def test_edge_case_n_20(self):
        self.assertEqual(nth_super_ugly_number(20, [2, 7, 13, 19]), 38)

    def test_edge_case_n_21(self):
        self.assertEqual(nth_super_ugly_number(21, [2, 7, 13, 19]), 40)

    def test_edge_case_n_22(self):
        self.assertEqual(nth_super_ugly_number(22, [2, 7, 13, 19]), 42)

    def test_edge_case_n_23(self):
        self.assertEqual(nth_super_ugly_number(23, [2, 7, 13, 19]), 44)

    def test_edge_case_n_24(self):
        self.assertEqual(nth_super_ugly_number(24, [2, 7, 13, 19]), 46)

    def test_edge_case_n_25(self):
        self.assertEqual(nth_super_ugly_number(25, [2, 7, 13, 19]),
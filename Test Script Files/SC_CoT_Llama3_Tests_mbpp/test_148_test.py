import unittest
from mbpp_148_code import sum_digits_twoparts

class TestSumDigitsTwoparts(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sum_digits_twoparts(123), 6)

    def test_edge_case(self):
        self.assertEqual(sum_digits_twoparts(999), 27)

    def test_edge_case2(self):
        self.assertEqual(sum_digits_twoparts(1000), 1)

    def test_edge_case3(self):
        self.assertEqual(sum_digits_twoparts(0), 0)

    def test_edge_case4(self):
        self.assertEqual(sum_digits_twoparts(1), 1)

    def test_edge_case5(self):
        self.assertEqual(sum_digits_twoparts(9), 9)

    def test_edge_case6(self):
        self.assertEqual(sum_digits_twoparts(10), 1)

    def test_edge_case7(self):
        self.assertEqual(sum_digits_twoparts(100), 1)

    def test_edge_case8(self):
        self.assertEqual(sum_digits_twoparts(12345), 15)

    def test_edge_case9(self):
        self.assertEqual(sum_digits_twoparts(123456), 21)

    def test_edge_case10(self):
        self.assertEqual(sum_digits_twoparts(1234567), 28)

    def test_edge_case11(self):
        self.assertEqual(sum_digits_twoparts(123456789), 45)

    def test_edge_case12(self):
        self.assertEqual(sum_digits_twoparts(1234567890), 45)

    def test_edge_case13(self):
        self.assertEqual(sum_digits_twoparts(12345678901), 45)

    def test_edge_case14(self):
        self.assertEqual(sum_digits_twoparts(123456789012), 45)

    def test_edge_case15(self):
        self.assertEqual(sum_digits_twoparts(1234567890123), 45)

    def test_edge_case16(self):
        self.assertEqual(sum_digits_twoparts(12345678901234), 45)

    def test_edge_case17(self):
        self.assertEqual(sum_digits_twoparts(123456789012345), 45)

    def test_edge_case18(self):
        self.assertEqual(sum_digits_twoparts(1234567890123456), 45)

    def test_edge_case19(self):
        self.assertEqual(sum_digits_twoparts(12345678901234567), 45)

    def test_edge_case20(self):
        self.assertEqual(sum_digits_twoparts(123456789012345678), 45)

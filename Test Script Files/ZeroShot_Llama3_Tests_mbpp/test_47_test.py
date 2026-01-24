import unittest
from mbpp_47_code import compute_Last_Digit

class TestComputeLastDigit(unittest.TestCase):

    def test_equal_A_and_B(self):
        self.assertEqual(compute_Last_Digit(10, 10), 1)

    def test_B_greater_than_A_by_5(self):
        self.assertEqual(compute_Last_Digit(10, 15), 0)

    def test_B_greater_than_A_by_4(self):
        self.assertEqual(compute_Last_Digit(10, 14), 0)

    def test_B_greater_than_A_by_3(self):
        self.assertEqual(compute_Last_Digit(10, 13), 0)

    def test_B_greater_than_A_by_2(self):
        self.assertEqual(compute_Last_Digit(10, 12), 0)

    def test_B_greater_than_A_by_1(self):
        self.assertEqual(compute_Last_Digit(10, 11), 0)

    def test_B_greater_than_A_by_0(self):
        self.assertEqual(compute_Last_Digit(10, 10), 0)

    def test_B_greater_than_A_by_minus_1(self):
        self.assertEqual(compute_Last_Digit(10, 9), 0)

    def test_B_greater_than_A_by_minus_2(self):
        self.assertEqual(compute_Last_Digit(10, 8), 0)

    def test_B_greater_than_A_by_minus_3(self):
        self.assertEqual(compute_Last_Digit(10, 7), 0)

    def test_B_greater_than_A_by_minus_4(self):
        self.assertEqual(compute_Last_Digit(10, 6), 0)

    def test_B_greater_than_A_by_minus_5(self):
        self.assertEqual(compute_Last_Digit(10, 5), 0)

    def test_B_greater_than_A_by_minus_6(self):
        self.assertEqual(compute_Last_Digit(10, 4), 0)

    def test_B_greater_than_A_by_minus_7(self):
        self.assertEqual(compute_Last_Digit(10, 3), 0)

    def test_B_greater_than_A_by_minus_8(self):
        self.assertEqual(compute_Last_Digit(10, 2), 0)

    def test_B_greater_than_A_by_minus_9(self):
        self.assertEqual(compute_Last_Digit(10, 1), 0)

    def test_B_greater_than_A_by_minus_10(self):
        self.assertEqual(compute_Last_Digit(10, 0), 0)

    def test_B_greater_than_A_by_minus_11(self):
        self.assertEqual(compute_Last_Digit(10, -1), 0)

    def test_B_greater_than_A_by_minus_12(self):
        self.assertEqual(compute_Last_Digit(10, -2), 0)

    def test_B_greater_than_A_by_minus_13(self):
        self.assertEqual(compute_Last_Digit(10, -3), 0)

    def test_B_greater_than_A_by_minus_14(self):
        self.assertEqual(compute_Last_Digit(10, -4), 0)

    def test_B_greater_than_A_by_minus_15(self):
        self.assertEqual(compute_Last_Digit(10, -5), 0)

    def test_B_greater_than_A_by_minus_16(self):
        self.assertEqual(compute_Last_Digit(10, -6), 0)

    def test_B_greater_than_A_by_minus_17(self):
        self.assertEqual(compute_Last_Digit(10, -7), 0)

    def test_B_greater_than_A_by_minus_18(self):
        self.assertEqual(compute_Last_Digit(10, -8), 0)

    def test_B_greater_than_A_by_minus_19(self):
        self.assertEqual(compute_Last_Digit(10, -9), 0)

    def test_B_greater_than_A_by_minus_20(self):
        self.assertEqual(compute_Last_Digit(10, -10), 0)

    def test_B_greater_than_A_by_minus_21(self):
        self.assertEqual(compute_Last_Digit(10, -11), 0)

    def test_B_greater_than_A_by_minus_22(self):
        self.assertEqual(compute_Last_Digit(10, -12), 0)

    def test_B_greater_than_A_by_minus_23(self):
        self.assertEqual(compute_Last_Digit(10, -13), 0)

    def test_B_greater_than_A_by_minus_24(self):
        self.assertEqual(compute_Last_Digit(10, -14), 0)

    def test_B_greater_than_A_by_minus_25(self):
        self.assertEqual(compute_Last_Digit(10, -15), 0)

    def test_B_greater_than_A_by_minus_26(self):
        self.assertEqual(compute_Last_Digit(10, -16), 0)

    def test_B_greater_than_A_by_minus_27(self):
        self.assertEqual(compute_Last_Digit
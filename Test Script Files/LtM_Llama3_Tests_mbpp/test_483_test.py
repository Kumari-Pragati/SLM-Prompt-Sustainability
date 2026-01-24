import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)

    def test_edge_case_x_1(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_edge_case_x_2(self):
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)

    def test_edge_case_x_3(self):
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)

    def test_edge_case_x_4(self):
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)

    def test_edge_case_x_5(self):
        self.assertEqual(first_Factorial_Divisible_Number(5), 4)

    def test_edge_case_x_6(self):
        self.assertEqual(first_Factorial_Divisible_Number(6), 2)

    def test_edge_case_x_7(self):
        self.assertEqual(first_Factorial_Divisible_Number(7), 3)

    def test_edge_case_x_8(self):
        self.assertEqual(first_Factorial_Divisible_Number(8), 6)

    def test_edge_case_x_9(self):
        self.assertEqual(first_Factorial_Divisible_Number(9), 6)

    def test_edge_case_x_10(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 6)

    def test_edge_case_x_11(self):
        self.assertEqual(first_Factorial_Divisible_Number(11), 6)

    def test_edge_case_x_12(self):
        self.assertEqual(first_Factorial_Divisible_Number(12), 6)

    def test_edge_case_x_13(self):
        self.assertEqual(first_Factorial_Divisible_Number(13), 6)

    def test_edge_case_x_14(self):
        self.assertEqual(first_Factorial_Divisible_Number(14), 6)

    def test_edge_case_x_15(self):
        self.assertEqual(first_Factorial_Divisible_Number(15), 6)

    def test_edge_case_x_16(self):
        self.assertEqual(first_Factorial_Divisible_Number(16), 6)

    def test_edge_case_x_17(self):
        self.assertEqual(first_Factorial_Divisible_Number(17), 6)

    def test_edge_case_x_18(self):
        self.assertEqual(first_Factorial_Divisible_Number(18), 6)

    def test_edge_case_x_19(self):
        self.assertEqual(first_Factorial_Divisible_Number(19), 6)

    def test_edge_case_x_20(self):
        self.assertEqual(first_Factorial_Divisible_Number(20), 6)

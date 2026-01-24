import unittest
from mbpp_483_code import first_Factorial_Divisible_Number

class TestFirstFactorialDivisibleNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(first_Factorial_Divisible_Number(5), 2)

    def test_edge_case_x_1(self):
        self.assertEqual(first_Factorial_Divisible_Number(1), 1)

    def test_edge_case_x_2(self):
        self.assertEqual(first_Factorial_Divisible_Number(2), 1)

    def test_edge_case_x_3(self):
        self.assertEqual(first_Factorial_Divisible_Number(3), 2)

    def test_edge_case_x_4(self):
        self.assertEqual(first_Factorial_Divisible_Number(4), 2)

    def test_edge_case_x_5(self):
        self.assertEqual(first_Factorial_Divisible_Number(5), 2)

    def test_edge_case_x_6(self):
        self.assertEqual(first_Factorial_Divisible_Number(6), 3)

    def test_edge_case_x_7(self):
        self.assertEqual(first_Factorial_Divisible_Number(7), 3)

    def test_edge_case_x_8(self):
        self.assertEqual(first_Factorial_Divisible_Number(8), 4)

    def test_edge_case_x_9(self):
        self.assertEqual(first_Factorial_Divisible_Number(9), 4)

    def test_edge_case_x_10(self):
        self.assertEqual(first_Factorial_Divisible_Number(10), 4)

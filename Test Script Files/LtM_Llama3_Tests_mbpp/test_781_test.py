import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_even_divisors(self):
        self.assertEqual(count_Divisors(4), "Even")

    def test_odd_divisors(self):
        self.assertEqual(count_Divisors(5), "Odd")

    def test_divisor_count_even(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_divisor_count_odd(self):
        self.assertEqual(count_Divisors(25), "Odd")

    def test_divisor_count_edge_case(self):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_divisor_count_edge_case2(self):
        self.assertEqual(count_Divisors(2), "Odd")

    def test_divisor_count_edge_case3(self):
        self.assertEqual(count_Divisors(3), "Odd")

    def test_divisor_count_edge_case4(self):
        self.assertEqual(count_Divisors(4), "Even")

    def test_divisor_count_edge_case5(self):
        self.assertEqual(count_Divisors(9), "Odd")

    def test_divisor_count_edge_case6(self):
        self.assertEqual(count_Divisors(10), "Even")

    def test_divisor_count_edge_case7(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_divisor_count_edge_case8(self):
        self.assertEqual(count_Divisors(15), "Odd")

    def test_divisor_count_edge_case9(self):
        self.assertEqual(count_Divisors(20), "Even")

    def test_divisor_count_edge_case10(self):
        self.assertEqual(count_Divisors(25), "Odd")

    def test_divisor_count_edge_case11(self):
        self.assertEqual(count_Divisors(30), "Even")

    def test_divisor_count_edge_case12(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_divisor_count_edge_case13(self):
        self.assertEqual(count_Divisors(40), "Even")

    def test_divisor_count_edge_case14(self):
        self.assertEqual(count_Divisors(45), "Odd")

    def test_divisor_count_edge_case15(self):
        self.assertEqual(count_Divisors(50), "Even")

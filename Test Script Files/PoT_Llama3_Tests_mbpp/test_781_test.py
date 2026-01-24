import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_edge_case(self):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_edge_case2(self):
        self.assertEqual(count_Divisors(2), "Even")

    def test_edge_case3(self):
        self.assertEqual(count_Divisors(3), "Odd")

    def test_edge_case4(self):
        self.assertEqual(count_Divisors(4), "Even")

    def test_edge_case5(self):
        self.assertEqual(count_Divisors(5), "Odd")

    def test_edge_case6(self):
        self.assertEqual(count_Divisors(6), "Even")

    def test_edge_case7(self):
        self.assertEqual(count_Divisors(7), "Odd")

    def test_edge_case8(self):
        self.assertEqual(count_Divisors(8), "Even")

    def test_edge_case9(self):
        self.assertEqual(count_Divisors(9), "Odd")

    def test_edge_case10(self):
        self.assertEqual(count_Divisors(10), "Even")

    def test_edge_case11(self):
        self.assertEqual(count_Divisors(11), "Odd")

    def test_edge_case12(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_edge_case13(self):
        self.assertEqual(count_Divisors(13), "Odd")

    def test_edge_case14(self):
        self.assertEqual(count_Divisors(14), "Even")

    def test_edge_case15(self):
        self.assertEqual(count_Divisors(15), "Odd")

    def test_edge_case16(self):
        self.assertEqual(count_Divisors(16), "Even")

    def test_edge_case17(self):
        self.assertEqual(count_Divisors(17), "Odd")

    def test_edge_case18(self):
        self.assertEqual(count_Divisors(18), "Even")

    def test_edge_case19(self):
        self.assertEqual(count_Divisors(19), "Odd")

    def test_edge_case20(self):
        self.assertEqual(count_Divisors(20), "Even")

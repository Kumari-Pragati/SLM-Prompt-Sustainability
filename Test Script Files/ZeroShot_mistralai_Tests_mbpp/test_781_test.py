import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_count_divisors_simple_numbers(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(3), "Odd")
        self.assertEqual(count_Divisors(4), "Even")
        self.assertEqual(count_Divisors(5), "Odd")
        self.assertEqual(count_Divisors(6), "Even")

    def test_count_divisors_small_numbers(self):
        self.assertEqual(count_Divisors(7), "Odd")
        self.assertEqual(count_Divisors(8), "Even")
        self.assertEqual(count_Divisors(9), "Odd")
        self.assertEqual(count_Divisors(10), "Even")
        self.assertEqual(count_Divisors(11), "Odd")
        self.assertEqual(count_Divisors(12), "Even")
        self.assertEqual(count_Divisors(13), "Odd")
        self.assertEqual(count_Divisors(14), "Even")
        self.assertEqual(count_Divisors(15), "Odd")
        self.assertEqual(count_Divisors(16), "Even")

    def test_count_divisors_large_numbers(self):
        self.assertEqual(count_Divisors(100), "Even")
        self.assertEqual(count_Divisors(101), "Odd")
        self.assertEqual(count_Divisors(102), "Even")
        self.assertEqual(count_Divisors(103), "Odd")
        self.assertEqual(count_Divisors(104), "Even")
        self.assertEqual(count_Divisors(105), "Odd")
        self.assertEqual(count_Divisors(106), "Even")
        self.assertEqual(count_Divisors(107), "Odd")
        self.assertEqual(count_Divisors(108), "Even")
        self.assertEqual(count_Divisors(109), "Odd")
        self.assertEqual(count_Divisors(110), "Even")

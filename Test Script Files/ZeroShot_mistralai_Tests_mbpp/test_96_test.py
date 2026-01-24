import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_divisor_of_one(self):
        self.assertEqual(divisor(1), 1)

    def test_divisor_of_two(self):
        self.assertEqual(divisor(2), 1)

    def test_divisor_of_three(self):
        self.assertEqual(divisor(3), 2)

    def test_divisor_of_four(self):
        self.assertEqual(divisor(4), 2)

    def test_divisor_of_five(self):
        self.assertEqual(divisor(5), 2)

    def test_divisor_of_six(self):
        self.assertEqual(divisor(6), 2)

    def test_divisor_of_seven(self):
        self.assertEqual(divisor(7), 1)

    def test_divisor_of_eight(self):
        self.assertEqual(divisor(8), 2)

    def test_divisor_of_nine(self):
        self.assertEqual(divisor(9), 3)

    def test_divisor_of_ten(self):
        self.assertEqual(divisor(10), 2)

    def test_divisor_of_twelve(self):
        self.assertEqual(divisor(12), 6)

    def test_divisor_of_prime_number(self):
        self.assertEqual(divisor(17), 1)

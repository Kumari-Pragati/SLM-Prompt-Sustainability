import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_find_divisor_equal_numbers(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_find_divisor_same_sign(self):
        self.assertEqual(find_Divisor(10, 2), 2)
        self.assertEqual(find_Divisor(-10, -2), -2)

    def test_find_divisor_opposite_signs(self):
        self.assertNotEqual(find_Divisor(10, -2), 2)
        self.assertNotEqual(find_Divisor(-10, 2), -2)

    def test_find_divisor_zero(self):
        self.assertEqual(find_Divisor(0, 5), 2)
        self.assertEqual(find_Divisor(5, 0), 2)

    def test_find_divisor_negative_zero(self):
        self.assertEqual(find_Divisor(0, -5), 2)
        self.assertEqual(find_Divisor(-5, 0), 2)

    def test_find_divisor_large_numbers(self):
        self.assertEqual(find_Divisor(1000000, 2), 2)
        self.assertEqual(find_Divisor(2, 1000000), 2)

import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_find_divisor_equal(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_find_divisor_same_number(self):
        self.assertEqual(find_Divisor(4, 4), 4)

    def test_find_divisor_different_numbers(self):
        self.assertEqual(find_Divisor(6, 3), 2)

    def test_find_divisor_zero(self):
        self.assertEqual(find_Divisor(0, 5), 2)
        self.assertEqual(find_Divisor(5, 0), 2)

    def test_find_divisor_negative_numbers(self):
        self.assertEqual(find_Divisor(-3, -2), 2)
        self.assertEqual(find_Divisor(-2, -3), 2)

    def test_find_divisor_invalid_input(self):
        self.assertRaises(TypeError, find_Divisor, "string", 5)
        self.assertRaises(TypeError, find_Divisor, 5, "string")

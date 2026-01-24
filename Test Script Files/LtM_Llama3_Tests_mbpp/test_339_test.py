import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):
    def test_equal_inputs(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_non_equal_inputs(self):
        self.assertEqual(find_Divisor(5, 3), 2)

    def test_same_input(self):
        self.assertEqual(find_Divisor(5, 5), 5)

    def test_zero_input(self):
        with self.assertRaises(TypeError):
            find_Divisor(0, 5)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            find_Divisor(-5, 5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_Divisor('a', 5)

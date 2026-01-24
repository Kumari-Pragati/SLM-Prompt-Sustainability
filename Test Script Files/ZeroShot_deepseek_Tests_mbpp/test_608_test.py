import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(bell_Number(0), 1)

    def test_positive_numbers(self):
        self.assertEqual(bell_Number(1), 2)
        self.assertEqual(bell_Number(2), 5)
        self.assertEqual(bell_Number(3), 15)
        self.assertEqual(bell_Number(4), 52)
        self.assertEqual(bell_Number(5), 203)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            bell_Number(-1)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            bell_Number(1.5)

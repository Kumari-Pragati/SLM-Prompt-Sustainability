import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_bell_number_zero(self):
        self.assertEqual(bell_Number(0), 1)

    def test_bell_number_one(self):
        self.assertEqual(bell_Number(1), 1)

    def test_bell_number_two(self):
        self.assertEqual(bell_Number(2), 2)

    def test_bell_number_three(self):
        self.assertEqual(bell_Number(3), 3)

    def test_bell_number_four(self):
        self.assertEqual(bell_Number(4), 5)

    def test_bell_number_five(self):
        self.assertEqual(bell_Number(5), 8)

    def test_bell_number_six(self):
        self.assertEqual(bell_Number(6), 13)

    def test_bell_number_negative(self):
        with self.assertRaises(ValueError):
            bell_Number(-1)

    def test_bell_number_non_integer(self):
        with self.assertRaises(TypeError):
            bell_Number(3.5)

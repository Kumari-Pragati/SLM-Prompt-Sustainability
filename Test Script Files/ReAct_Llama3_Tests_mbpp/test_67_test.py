import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_bell_number_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_bell_number_one(self):
        self.assertEqual(bell_number(1), 1)

    def test_bell_number_two(self):
        self.assertEqual(bell_number(2), 2)

    def test_bell_number_three(self):
        self.assertEqual(bell_number(3), 3)

    def test_bell_number_four(self):
        self.assertEqual(bell_number(4), 5)

    def test_bell_number_five(self):
        self.assertEqual(bell_number(5), 8)

    def test_bell_number_negative(self):
        with self.assertRaises(TypeError):
            bell_number(-1)

    def test_bell_number_non_integer(self):
        with self.assertRaises(TypeError):
            bell_number('a')

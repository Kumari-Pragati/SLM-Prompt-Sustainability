import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_bell_number_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_bell_number_one(self):
        self.assertEqual(bell_number(1), 2)

    def test_bell_number_two(self):
        self.assertEqual(bell_number(2), 5)

    def test_bell_number_three(self):
        self.assertEqual(bell_number(3), 15)

    def test_bell_number_negative(self):
        with self.assertRaises(Exception):
            bell_number(-1)

    def test_bell_number_large(self):
        with self.assertRaises(Exception):
            bell_number(1000)

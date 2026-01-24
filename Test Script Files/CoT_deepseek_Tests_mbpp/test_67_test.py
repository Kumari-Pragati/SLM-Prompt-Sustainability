import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bell_number(5), 52)

    def test_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_boundary_condition(self):
        self.assertEqual(bell_number(1), 2)
        self.assertEqual(bell_number(2), 5)

    def test_large_number(self):
        self.assertEqual(bell_number(10), 5025)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            bell_number(-1)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            bell_number(2.5)

    def test_string_input(self):
        with self.assertRaises(Exception):
            bell_number("test")

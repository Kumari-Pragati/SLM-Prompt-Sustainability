import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bell_Number(5), 52)

    def test_zero_case(self):
        self.assertEqual(bell_Number(0), 1)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            bell_Number(-1)

    def test_large_number_case(self):
        self.assertEqual(bell_Number(10), 5025)

    def test_non_integer_case(self):
        with self.assertRaises(Exception):
            bell_Number(1.5)

    def test_string_case(self):
        with self.assertRaises(Exception):
            bell_Number("test")

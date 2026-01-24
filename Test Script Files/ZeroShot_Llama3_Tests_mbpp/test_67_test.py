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
        self.assertEqual(bell_number(3), 5)

    def test_bell_number_four(self):
        self.assertEqual(bell_number(4), 15)

    def test_bell_number_five(self):
        self.assertEqual(bell_number(5), 52)

    def test_bell_number_six(self):
        self.assertEqual(bell_number(6), 203)

    def test_bell_number_seven(self):
        self.assertEqual(bell_number(7), 742)

    def test_bell_number_eight(self):
        self.assertEqual(bell_number(8), 2673)

    def test_bell_number_nine(self):
        self.assertEqual(bell_number(9), 9228)

    def test_bell_number_ten(self):
        self.assertEqual(bell_number(10), 373504)

import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_bell_number_with_zero(self):
        self.assertEqual(bell_number(0), 1)

    def test_bell_number_with_one(self):
        self.assertEqual(bell_number(1), 1)

    def test_bell_number_with_two(self):
        self.assertEqual(bell_number(2), 2)

    def test_bell_number_with_three(self):
        self.assertEqual(bell_number(3), 4)

    def test_bell_number_with_four(self):
        self.assertEqual(bell_number(4), 10)

    def test_bell_number_with_five(self):
        self.assertEqual(bell_number(5), 20)

    def test_bell_number_with_large_input(self):
        self.assertEqual(bell_number(100), 3527187803071342865)

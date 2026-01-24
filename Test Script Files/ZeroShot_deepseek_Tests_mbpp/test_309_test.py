import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_maximum_with_equal_numbers(self):
        self.assertEqual(maximum(5, 5), 5)

    def test_maximum_with_first_greater(self):
        self.assertEqual(maximum(10, 5), 10)

    def test_maximum_with_second_greater(self):
        self.assertEqual(maximum(5, 10), 10)

    def test_maximum_with_negative_numbers(self):
        self.assertEqual(maximum(-10, -5), -5)

    def test_maximum_with_zero(self):
        self.assertEqual(maximum(0, 5), 5)
        self.assertEqual(maximum(5, 0), 5)
        self.assertEqual(maximum(0, 0), 0)

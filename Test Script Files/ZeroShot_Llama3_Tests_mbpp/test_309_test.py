import unittest
from mbpp_309_code import maximum

class TestMaximumFunction(unittest.TestCase):

    def test_maximum_equal(self):
        self.assertEqual(maximum(5, 5), 5)

    def test_maximum_a_greater(self):
        self.assertEqual(maximum(10, 5), 10)

    def test_maximum_b_greater(self):
        self.assertEqual(maximum(5, 10), 10)

    def test_maximum_negative(self):
        self.assertEqual(maximum(-5, -10), -5)

    def test_maximum_zero(self):
        self.assertEqual(maximum(0, 0), 0)

    def test_maximum_zero_and_positive(self):
        self.assertEqual(maximum(0, 5), 5)

    def test_maximum_positive_and_zero(self):
        self.assertEqual(maximum(5, 0), 5)

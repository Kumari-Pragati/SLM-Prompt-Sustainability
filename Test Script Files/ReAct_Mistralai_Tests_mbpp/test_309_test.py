import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(maximum(5, 3), 5)
        self.assertEqual(maximum(3, 5), 5)
        self.assertEqual(maximum(100, 99), 100)
        self.assertEqual(maximum(99, 100), 100)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(maximum(0, 5), 5)
        self.assertEqual(maximum(5, 0), 5)

    def test_negative_numbers(self):
        self.assertEqual(maximum(-3, -5), -3)
        self.assertEqual(maximum(-5, -3), -3)
        self.assertEqual(maximum(-100, -99), -100)
        self.assertEqual(maximum(-99, -100), -100)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(maximum(0, -5), -5)
        self.assertEqual(maximum(-5, 0), -5)

    def test_edge_cases(self):
        self.assertEqual(maximum(-1, 1), 1)
        self.assertEqual(maximum(1, -1), 1)
        self.assertEqual(maximum(-0.001, 0.001), 0.001)
        self.assertEqual(maximum(0.001, -0.001), 0.001)
        self.assertEqual(maximum(-float('inf'), float('inf')), float('inf'))
        self.assertEqual(maximum(float('inf'), -float('inf')), float('inf'))

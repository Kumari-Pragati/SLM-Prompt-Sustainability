import unittest
from mbpp_404_code import minimum

class TestMinimumFunction(unittest.TestCase):

    def test_minimum_positive_numbers(self):
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(2, 1), 1)
        self.assertEqual(minimum(3, 4), 3)
        self.assertEqual(minimum(4, 3), 3)

    def test_minimum_zero_and_positive_numbers(self):
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(1, 0), 0)
        self.assertEqual(minimum(0, 3), 0)
        self.assertEqual(minimum(3, 0), 0)

    def test_minimum_negative_numbers(self):
        self.assertEqual(minimum(-1, -2), -1)
        self.assertEqual(minimum(-2, -1), -2)
        self.assertEqual(minimum(-3, -4), -3)
        self.assertEqual(minimum(-4, -3), -4)

    def test_minimum_zero_and_negative_numbers(self):
        self.assertEqual(minimum(0, -1), -1)
        self.assertEqual(minimum(-1, 0), -1)
        self.assertEqual(minimum(0, -3), 0)
        self.assertEqual(minimum(-3, 0), -3)

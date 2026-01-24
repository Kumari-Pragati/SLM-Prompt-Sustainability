import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_same_value(self):
        self.assertEqual(minimum(3, 3), 3)

    def test_smaller_value(self):
        self.assertEqual(minimum(2, 3), 2)

    def test_larger_value(self):
        self.assertEqual(minimum(3, 2), 2)

    def test_zero(self):
        self.assertEqual(minimum(0, 3), 0)

    def test_negative_numbers(self):
        self.assertEqual(minimum(-2, -3), -3)

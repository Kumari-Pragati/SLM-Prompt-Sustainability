import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):
    def test_equal_values(self):
        self.assertEqual(minimum(2, 2), 2)

    def test_a_smaller_than_b(self):
        self.assertEqual(minimum(1, 3), 1)

    def test_b_smaller_than_a(self):
        self.assertEqual(minimum(3, 1), 1)

    def test_negative_values(self):
        self.assertEqual(minimum(-1, -2), -2)

    def test_zero_values(self):
        self.assertEqual(minimum(0, 0), 0)

    def test_non_integer_values(self):
        self.assertEqual(minimum(2.5, 3.5), 2.5)

import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_minimum_a_less_than_b(self):
        self.assertEqual(minimum(1, 2), 1)

    def test_minimum_b_less_than_a(self):
        self.assertEqual(minimum(3, 2), 2)

    def test_minimum_equal_numbers(self):
        self.assertEqual(minimum(2, 2), 2)

    def test_minimum_negative_numbers(self):
        self.assertEqual(minimum(-1, -3), -3)

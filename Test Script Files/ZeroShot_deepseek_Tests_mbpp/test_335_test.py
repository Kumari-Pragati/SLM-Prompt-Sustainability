import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(ap_sum(1, 5, 2), 14)
        self.assertEqual(ap_sum(10, 10, 1), 100)
        self.assertEqual(ap_sum(0, 10, 1), 45)

    def test_negative_numbers(self):
        self.assertEqual(ap_sum(-1, 5, 2), 8)
        self.assertEqual(ap_sum(-10, 10, 1), -45)
        self.assertEqual(ap_sum(0, 10, -1), -45)

    def test_zero_numbers(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            ap_sum("a", 5, 2)
        with self.assertRaises(TypeError):
            ap_sum(1, "a", 2)
        with self.assertRaises(TypeError):
            ap_sum(1, 5, "a")

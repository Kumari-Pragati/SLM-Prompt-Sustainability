import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum(4, 6), 2)
        self.assertEqual(sum(6, 4), 2)
        self.assertEqual(sum(2, 2), 2)

    def test_zero(self):
        self.assertEqual(sum(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum(-2, -3), 1)
        self.assertEqual(sum(-3, -2), 1)

    def test_one_argument(self):
        self.assertEqual(sum(4), 0)
        self.assertEqual(sum(-4), 0)

    def test_large_numbers(self):
        self.assertEqual(sum(1000000, 1000000), 1000000)

    def test_mixed_numbers(self):
        self.assertEqual(sum(4, -3), 1)
        self.assertEqual(sum(-4, 3), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum, 'a', 3)
        self.assertRaises(TypeError, sum, 3, 'b')

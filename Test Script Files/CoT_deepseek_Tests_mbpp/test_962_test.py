import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Even(2, 10), 20)

    def test_large_range(self):
        self.assertEqual(sum_Even(1, 1000000), 250000250000)

    def test_single_number(self):
        self.assertEqual(sum_Even(2, 2), 0)

    def test_negative_range(self):
        self.assertEqual(sum_Even(-10, 10), 0)

    def test_zero_range(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Even("2", 10)

import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_empty_range(self):
        self.assertEqual(sum_Even(0, 0), 0)

    def test_single_number(self):
        for n in range(1, 11):
            self.assertEqual(sum_Even(n, n), sum_Natural(n))

    def test_even_range(self):
        for i in range(2, 11):
            self.assertEqual(sum_Even(2, i * 2), sum_Natural(i))

    def test_odd_range(self):
        for i in range(1, 11):
            self.assertEqual(sum_Even(i, (i * 2) + 1), sum_Natural(i) - 1)

    def test_negative_range(self):
        self.assertEqual(sum_Even(-1, 0), 0)
        self.assertEqual(sum_Even(0, 1), 1)
        self.assertEqual(sum_Even(1, 2), 3)
        self.assertEqual(sum_Even(2, 3), 0)

    def test_large_range(self):
        self.assertEqual(sum_Even(1000000, 2000000), sum_Natural(1000000) - sum_Natural(0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Even('a', 'b')
        with self.assertRaises(TypeError):
            sum_Even(1.5, 2)
        with self.assertRaises(ValueError):
            sum_Even(0, -1)

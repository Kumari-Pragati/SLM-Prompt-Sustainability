import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(find_lucas(0), 2)
        self.assertEqual(find_lucas(1), 1)

    def test_positive_numbers(self):
        for n in range(2, 10):
            self.assertEqual(find_lucas(n), find_lucas(n - 1) + find_lucas(n - 2))

    def test_large_number(self):
        self.assertEqual(find_lucas(100), find_lucas(99) + find_lucas(98))

    def test_negative_numbers(self):
        with self.subTest('negative_zero'):
            self.assertEqual(find_lucas(-1), ValueError)
        with self.subTest('negative_one'):
            self.assertEqual(find_lucas(-2), ValueError)
        with self.subTest('negative_two'):
            self.assertEqual(find_lucas(-3), 2)

    def test_floats(self):
        with self.subTest('float_zero'):
            self.assertEqual(find_lucas(0.0), 2)
        with self.subTest('float_one'):
            self.assertEqual(find_lucas(1.0), 1)
        with self.subTest('float_large'):
            self.assertEqual(find_lucas(100.0), find_lucas(99.0) + find_lucas(98.0))

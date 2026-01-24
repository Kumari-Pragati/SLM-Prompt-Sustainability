import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(multiply_num([1, 2, 3]), 2.0)
        self.assertEqual(multiply_num([4, 5, 6]), 12.0)
        self.assertEqual(multiply_num([7, 8, 9]), 28.0)

    def test_empty_input(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_single_element(self):
        self.assertEqual(multiply_num([1]), 1.0)
        self.assertEqual(multiply_num([5]), 5.0)

    def test_negative_numbers(self):
        self.assertEqual(multiply_num([-1, 2, 3]), 1.0)
        self.assertEqual(multiply_num([1, -2, 3]), 1.0)

    def test_zero_in_input(self):
        self.assertEqual(multiply_num([0, 1, 2]), 1.0)
        self.assertEqual(multiply_num([1, 0, 2]), 1.0)

    def test_large_numbers(self):
        self.assertEqual(multiply_num([100, 200, 300]), 100.0)
        self.assertEqual(multiply_num([1000, 2000, 3000]), 6000.0)

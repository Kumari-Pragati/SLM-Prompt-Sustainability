import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_single_element(self):
        self.assertEqual(_sum([5]), 5)

    def test_empty_list(self):
        self.assertEqual(_sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 3)

    def test_large_numbers(self):
        self.assertEqual(_sum(list(range(1, 10001))), 50005000)

    def test_float_numbers(self):
        self.assertAlmostEqual(_sum([1.1, 2.2, 3.3, 4.4]), 11.0)

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            _sum(['1', '2', '3'])

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            _sum(123)

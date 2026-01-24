import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_Even([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_Even([2]), 2)

    def test_even_elements(self):
        self.assertEqual(sum_Even([2, 4, 6, 8]), 20)

    def test_odd_elements(self):
        self.assertEqual(sum_Even([1, 3, 5, 7]), 10)

    def test_mixed_elements(self):
        self.assertEqual(sum_Even([1, 2, 3, 4, 5, 6]), 20)

    def test_large_list(self):
        self.assertEqual(sum_Even(list(range(20, 41))), 630)

    def test_negative_numbers(self):
        self.assertEqual(sum_Even([-2, -4, -6]), -6)

    def test_floating_point_input(self):
        self.assertEqual(sum_Even([2.5, 4.5, 6.5]), 10)

    def test_non_integer_input(self):
        self.assertEqual(sum_Even(["2", "4", "6"]), TracebackError)

    def test_empty_range(self):
        self.assertEqual(sum_Even(range(0, 0)), 0)

    def test_invalid_range(self):
        self.assertRaises(ValueError, sum_Even, (1, -1))

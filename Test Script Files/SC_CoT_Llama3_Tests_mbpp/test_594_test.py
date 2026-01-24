import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(diff_even_odd([2, 4, 6, 8]), 0)
        self.assertEqual(diff_even_odd([1, 3, 5, 7]), 0)
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10]), 0)
        self.assertEqual(diff_even_odd([1, 3, 5, 7, 9]), 0)

    def test_edge_cases(self):
        self.assertEqual(diff_even_odd([2]), 2)
        self.assertEqual(diff_even_odd([1]), -1)
        self.assertEqual(diff_even_odd([2, 1]), 1)
        self.assertEqual(diff_even_odd([1, 2]), -1)

    def test_special_cases(self):
        self.assertEqual(diff_even_odd([]), -1)
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 0]), 0)
        self.assertEqual(diff_even_odd([1, 3, 5, 7, 0]), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            diff_even_odd('abc')
        with self.assertRaises(TypeError):
            diff_even_odd(None)
        with self.assertRaises(TypeError):
            diff_even_odd({1, 2, 3})

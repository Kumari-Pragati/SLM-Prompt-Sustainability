import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(diff_even_odd([2, 4, 6]), 2)
        self.assertEqual(diff_even_odd([1, 3, 5]), -2)
        self.assertEqual(diff_even_odd([2, 1, 4, 3, 6, 5]), 2)

    def test_edge_cases(self):
        self.assertEqual(diff_even_odd([]), -1)
        self.assertEqual(diff_even_odd([2]), 2)
        self.assertEqual(diff_even_odd([1]), -1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            diff_even_odd("string")
        with self.assertRaises(TypeError):
            diff_even_odd(123)

import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4]), 2)
        self.assertEqual(diff_even_odd([10, 15, 20]), 10)

    def test_edge_conditions(self):
        self.assertEqual(diff_even_odd([]), -1)
        self.assertEqual(diff_even_odd([1]), -1)
        self.assertEqual(diff_even_odd([1, 3, 5]), -1)
        self.assertEqual(diff_even_odd([2, 4, 6]), 0)

    def test_complex_cases(self):
        self.assertEqual(diff_even_odd([1, 3, 5, 7, 9]), -1)
        self.assertEqual(diff_even_odd([2, 4, 6, 8, 10]), 0)
        self.assertEqual(diff_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

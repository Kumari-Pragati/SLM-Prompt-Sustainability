import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4]), 6)
        self.assertEqual(sum_even_odd([10, 15, 20]), 30)

    def test_edge_conditions(self):
        self.assertEqual(sum_even_odd([]), -1)
        self.assertEqual(sum_even_odd([1]), -1)
        self.assertEqual(sum_even_odd([2]), 2)
        self.assertEqual(sum_even_odd([1, 3]), -1)
        self.assertEqual(sum_even_odd([1, 2]), 3)

    def test_complex_cases(self):
        self.assertEqual(sum_even_odd([1, 3, 5, 7, 9]), -1)
        self.assertEqual(sum_even_odd([2, 4, 6, 8, 10]), 20)
        self.assertEqual(sum_even_odd([1, 3, 5, 2, 4]), 6)
        self.assertEqual(sum_even_odd([10, 9, 8, 7, 6]), 16)

import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4]), 6)

    def test_edge_condition(self):
        self.assertEqual(sum_even_odd([1, 9, 5, 7]), -1)

    def test_boundary_condition(self):
        self.assertEqual(sum_even_odd([2]), 2)
        self.assertEqual(sum_even_odd([1]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_even_odd("1, 2, 3, 4")

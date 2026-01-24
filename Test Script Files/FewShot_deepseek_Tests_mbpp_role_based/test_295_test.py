import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_div(6), 6)

    def test_edge_case(self):
        self.assertEqual(sum_div(1), 1)

    def test_boundary_case(self):
        self.assertEqual(sum_div(2), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_div('a')

    def test_zero(self):
        self.assertEqual(sum_div(0), 0)

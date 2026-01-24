import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_edge_condition(self):
        self.assertEqual(sum_positivenum([0]), 0)

    def test_boundary_condition(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_positivenum("1, 2, 3")

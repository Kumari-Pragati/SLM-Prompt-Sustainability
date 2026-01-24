import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 4)
        self.assertEqual(Sum(5), 5)

    def test_edge_conditions(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(Sum(100), 106)
        self.assertEqual(Sum(200), 220)

    def test_complex_cases(self):
        self.assertEqual(Sum(300), 330)
        self.assertEqual(Sum(400), 440)

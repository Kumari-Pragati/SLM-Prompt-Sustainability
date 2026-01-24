import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(closest_num(10), 9)
        self.assertEqual(closest_num(20), 19)

    def test_boundary_conditions(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(0), -1)
        self.assertEqual(closest_num(-1), -2)

    def test_edge_cases(self):
        self.assertEqual(closest_num(float('inf')), float('inf'))
        self.assertEqual(closest_num(float('-inf')), float('-inf'))

    def test_complex_cases(self):
        self.assertEqual(closest_num(10.5), 10.5)
        self.assertEqual(closest_num(0.1), 0.1)
        self.assertEqual(closest_num(-0.1), -0.1)

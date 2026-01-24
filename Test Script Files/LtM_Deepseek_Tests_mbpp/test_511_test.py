import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Min_Sum(10), 10)
        self.assertEqual(find_Min_Sum(15), 15)
        self.assertEqual(find_Min_Sum(20), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(0), 0)
        self.assertEqual(find_Min_Sum(2), 2)

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(find_Min_Sum(30), 30)
        self.assertEqual(find_Min_Sum(45), 45)
        self.assertEqual(find_Min_Sum(60), 60)
        self.assertEqual(find_Min_Sum(85), 85)
        self.assertEqual(find_Min_Sum(100), 100)

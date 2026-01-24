import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(4), 2)
        self.assertEqual(find_Min_Sum(16), 4)
        self.assertEqual(find_Min_Sum(25), 5)
        self.assertEqual(find_Min_Sum(36), 6)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Min_Sum, 'not_a_number')
        self.assertRaises(TypeError, find_Min_Sum, -1)
        self.assertRaises(TypeError, find_Min_Sum, 0)

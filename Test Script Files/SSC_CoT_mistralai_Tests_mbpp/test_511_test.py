import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(find_Min_Sum(12), 3)
        self.assertEqual(find_Min_Sum(20), 4)
        self.assertEqual(find_Min_Sum(28), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(4), 2)
        self.assertEqual(find_Min_Sum(6), 3)
        self.assertEqual(find_Min_Sum(10), 4)
        self.assertEqual(find_Min_Sum(15), 5)
        self.assertEqual(find_Min_Sum(24), 6)
        self.assertEqual(find_Min_Sum(30), 6)
        self.assertEqual(find_Min_Sum(42), 6)
        self.assertEqual(find_Min_Sum(60), 12)
        self.assertEqual(find_Min_Sum(100), 25)

    def test_special_cases(self):
        self.assertEqual(find_Min_Sum(4), 2)
        self.assertEqual(find_Min_Sum(9), 3)
        self.assertEqual(find_Min_Sum(25), 5)
        self.assertEqual(find_Min_Sum(49), 7)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_Min_Sum, 0)
        self.assertRaises(TypeError, find_Min_Sum, 'not_a_number')

import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Sum(12), 6)

    def test_boundary_conditions(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(0), 0)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 3)
        self.assertEqual(find_Min_Sum(4), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Min_Sum('abc')
        with self.assertRaises(TypeError):
            find_Min_Sum(None)
        with self.assertRaises(TypeError):
            find_Min_Sum([])

import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)

    def test_boundary_conditions(self):
        self.assertEqual(cal_sum(3), 9)
        self.assertEqual(cal_sum(4), 14)

    def test_edge_cases(self):
        self.assertEqual(cal_sum(5), 23)
        self.assertEqual(cal_sum(6), 34)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cal_sum('a')
        with self.assertRaises(ValueError):
            cal_sum(-1)

import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 14)

    def test_boundary_conditions(self):
        self.assertEqual(cal_sum(-1), 3)
        self.assertEqual(cal_sum(-10), 3)
        self.assertEqual(cal_sum(5), 26)
        self.assertEqual(cal_sum(10), 144)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            cal_sum('a')
        with self.assertRaises(TypeError):
            cal_sum(None)
        with self.assertRaises(TypeError):
            cal_sum([])

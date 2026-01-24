import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(ap_sum(1, 5, 2), 25)

    def test_edge_cases(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)
        self.assertEqual(ap_sum(0, 1, 0), 0)
        self.assertEqual(ap_sum(1, 0, 0), 0)
        self.assertEqual(ap_sum(1, 1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(ap_sum(1, 1, 1), 2)
        self.assertEqual(ap_sum(1, 2, 1), 6)
        self.assertEqual(ap_sum(1, 3, 1), 11)
        self.assertEqual(ap_sum(1, 4, 1), 18)
        self.assertEqual(ap_sum(1, 5, 1), 25)

    def test_negative_a(self):
        self.assertEqual(ap_sum(-1, 5, 2), 25)

    def test_negative_d(self):
        self.assertEqual(ap_sum(1, 5, -2), 25)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, ap_sum, 'a', 5, 2)
        self.assertRaises(TypeError, ap_sum, 1, 'n', 2)
        self.assertRaises(TypeError, ap_sum, 1, 5, 'd')
        self.assertRaises(ValueError, ap_sum, 0, 0, 0)
        self.assertRaises(ValueError, ap_sum, 0, 1, -1)
        self.assertRaises(ValueError, ap_sum, 1, 0, -1)

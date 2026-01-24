import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(ap_sum(1, 3, 2), 13)
        self.assertEqual(ap_sum(2, 4, 3), 42)

    def test_edge_cases(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)
        self.assertEqual(ap_sum(1, 1, 0), 1)
        self.assertEqual(ap_sum(1, 1, 1), 2)
        self.assertEqual(ap_sum(100, 100, 100), 50500)

    def test_negative_d(self):
        self.assertEqual(ap_sum(1, 3, -2), 3)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, ap_sum, 'a', 3, 2)
        self.assertRaises(TypeError, ap_sum, 1, 'n', 2)
        self.assertRaises(TypeError, ap_sum, 1, 3, 'd')
        self.assertRaises(ValueError, ap_sum, -1, 3, 2)
        self.assertRaises(ValueError, ap_sum, 1, 0, 2)
        self.assertRaises(ValueError, ap_sum, 1, -1, 2)

import unittest
from mbpp_335_code import ap_sum

class TestArithmeticProgressionSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(ap_sum(1, 5, 2), 14.5)

    def test_zero_elements(self):
        self.assertEqual(ap_sum(1, 0, 2), 0)

    def test_single_element(self):
        self.assertEqual(ap_sum(1, 1, 2), 1)

    def test_negative_elements(self):
        self.assertAlmostEqual(ap_sum(-1, 5, 2), 14.5)

    def test_zero_difference(self):
        self.assertEqual(ap_sum(1, 5, 0), 5)

    def test_negative_difference(self):
        self.assertAlmostEqual(ap_sum(1, 5, -2), 14.5)

    def test_invalid_n(self):
        with self.assertRaises(TypeError):
            ap_sum(1, 'five', 2)

    def test_invalid_d(self):
        with self.assertRaises(TypeError):
            ap_sum(1, 5, 'two')

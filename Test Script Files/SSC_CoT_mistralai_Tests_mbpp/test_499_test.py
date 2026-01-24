import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(diameter_circle(3), 6)

    def test_edge_cases(self):
        self.assertEqual(diameter_circle(0), 0)
        self.assertEqual(diameter_circle(1e-8), 2*1e-8)
        self.assertEqual(diameter_circle(1e30), 2*1e30)

    def test_negative_input(self):
        self.assertRaises(ValueError, diameter_circle, -1)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, diameter_circle, 'str')
        self.assertRaises(TypeError, diameter_circle, [1, 2, 3])

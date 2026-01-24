import unittest
from mbpp_139_code import circle_cumference

class TestCircleCircumference(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(circle_circumference(5), 31.4159, places=4)

    def test_edge_case_zero_radius(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference(-5)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            circle_circumference('five')

    def test_edge_case_large_radius(self):
        self.assertAlmostEqual(circle_circumference(100), 628.3185, places=4)

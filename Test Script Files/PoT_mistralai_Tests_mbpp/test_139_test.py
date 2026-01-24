import unittest
from mbpp_139_code import circle_circumference

class TestCircleCircumference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(circle_circumference(3), 18.849555921538738)

    def test_edge_case_zero(self):
        self.assertEqual(circle_circumference(0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(circle_circumference(-1), None)

    def test_boundary_case_one(self):
        self.assertEqual(circle_circumference(1), 6.283185307179586)

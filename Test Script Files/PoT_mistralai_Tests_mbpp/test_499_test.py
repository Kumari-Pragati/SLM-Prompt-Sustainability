import unittest
from mbpp_499_code import diameter_circle

class TestDiameterCircle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(diameter_circle(3), 6)

    def test_edge_case_zero(self):
        self.assertEqual(diameter_circle(0), None)

    def test_edge_case_negative(self):
        self.assertEqual(diameter_circle(-1), None)

    def test_boundary_case_one(self):
        self.assertEqual(diameter_circle(1), 2)

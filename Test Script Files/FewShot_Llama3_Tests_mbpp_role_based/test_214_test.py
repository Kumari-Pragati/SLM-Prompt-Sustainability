import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(degree_radian(0), 0)

    def test_edge_case_pi(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180)

    def test_edge_case_two_pi(self):
        self.assertAlmostEqual(degree_radian(2*math.pi), 360)

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            degree_radian('abc')

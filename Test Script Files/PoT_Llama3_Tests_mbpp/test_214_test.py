import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90, places=5)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(degree_radian(0), 0, places=5)

    def test_edge_case_pi(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180, places=5)

    def test_edge_case_two_pi(self):
        self.assertAlmostEqual(degree_radian(2*math.pi), 360, places=5)

    def test_edge_case_negative_pi(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180, places=5)

    def test_edge_case_negative_two_pi(self):
        self.assertAlmostEqual(degree_radian(-2*math.pi), -360, places=5)

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            degree_radian('a')

    def test_invalid_input_negative_zero(self):
        with self.assertRaises(TypeError):
            degree_radian(-0)

import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_simple_positive_radian(self):
        self.assertAlmostEqual(degree_radian(1), 57.29577951308232)

    def test_simple_negative_radian(self):
        self.assertAlmostEqual(degree_radian(-1), -57.29577951308232)

    def test_boundary_min_max(self):
        self.assertAlmostEqual(degree_radian(0), 0)
        self.assertAlmostEqual(degree_radian(math.pi), 180)

    def test_edge_case_zero_radian(self):
        self.assertEqual(degree_radian(0), 0)

    def test_edge_case_pi_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180)

    def test_complex_large_radian(self):
        self.assertAlmostEqual(degree_radian(2*math.pi), 360)

    def test_complex_negative_large_radian(self):
        self.assertAlmostEqual(degree_radian(-2*math.pi), -360)

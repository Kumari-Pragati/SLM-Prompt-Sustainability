import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(degree_radian(0), 0)
        self.assertEqual(degree_radian(math.pi / 2), 90)
        self.assertEqual(degree_radian(math.pi), 180)
        self.assertEqual(degree_radian(3 * math.pi / 2), 270)
        self.assertEqual(degree_radian(math.pi * 2), 360)

    def test_edge_and_boundary_cases(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180)
        self.assertAlmostEqual(degree_radian(math.pi * 2 + 0.001), 360)
        self.assertAlmostEqual(degree_radian(math.inf), None)
        self.assertAlmostEqual(degree_radian(-math.inf), None)

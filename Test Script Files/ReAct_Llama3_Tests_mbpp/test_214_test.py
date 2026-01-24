import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90, places=5)

    def test_edge_case(self):
        self.assertAlmostEqual(degree_radian(0), 0, places=5)
        self.assertAlmostEqual(degree_radian(math.pi), 180, places=5)

    def test_negative_radian(self):
        self.assertAlmostEqual(degree_radian(-math.pi/2), -90, places=5)

    def test_large_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi*2), 360, places=5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            degree_radian('invalid')

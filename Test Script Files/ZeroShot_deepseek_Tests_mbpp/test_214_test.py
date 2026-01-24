import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_positive_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi/2), 90.0, places=2)

    def test_negative_radian(self):
        self.assertAlmostEqual(degree_radian(-math.pi/2), -90.0, places=2)

    def test_zero_radian(self):
        self.assertEqual(degree_radian(0), 0)

    def test_large_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180.0, places=2)

    def test_small_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi/4), 45.0, places=2)

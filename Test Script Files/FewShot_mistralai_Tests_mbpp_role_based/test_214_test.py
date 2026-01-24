import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_positive_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi / 2), 90)

    def test_zero_radian(self):
        self.assertEqual(degree_radian(0), 0)

    def test_negative_radian(self):
        self.assertAlmostEqual(degree_radian(-math.pi / 2), -90)

    def test_large_positive_radian(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180)

    def test_large_negative_radian(self):
        self.assertAlmostEqual(degree_radian(-math.pi), -180)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            degree_radian(-1)

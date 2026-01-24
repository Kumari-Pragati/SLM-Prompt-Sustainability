import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(degree_radian(1), 57.29577951308232, places=5)

    def test_zero_input(self):
        self.assertEqual(degree_radian(0), 0)

    def test_large_input(self):
        self.assertAlmostEqual(degree_radian(1000), 57295.77951308232, places=5)

    def test_negative_input(self):
        self.assertAlmostEqual(degree_radian(-1), -57.29577951308232, places=5)

    def test_large_negative_input(self):
        self.assertAlmostEqual(degree_radian(-1000), -57295.77951308232, places=5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            degree_radian('a')

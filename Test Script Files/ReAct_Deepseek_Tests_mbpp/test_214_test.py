import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(degree_radian(1), 57.29577951308232, places=5)

    def test_zero_case(self):
        self.assertEqual(degree_radian(0), 0)

    def test_negative_case(self):
        self.assertAlmostEqual(degree_radian(-1), -57.29577951308232, places=5)

    def test_large_number_case(self):
        self.assertAlmostEqual(degree_radian(1000), 57295.77951308232, places=5)

    def test_large_negative_number_case(self):
        self.assertAlmostEqual(degree_radian(-1000), -57295.77951308232, places=5)

    def test_large_decimal_case(self):
        self.assertAlmostEqual(degree_radian(3.14159), 179.99999999999997, places=5)

    def test_large_negative_decimal_case(self):
        self.assertAlmostEqual(degree_radian(-3.14159), -179.99999999999997, places=5)

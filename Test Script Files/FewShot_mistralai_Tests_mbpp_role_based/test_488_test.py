import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(area_pentagon(3), 4.598076211359952)

    def test_zero(self):
        self.assertAlmostEqual(area_pentagon(0), 0.0)

    def test_negative_number(self):
        self.assertAlmostEqual(area_pentagon(-1), 0.0)

    def test_large_number(self):
        self.assertAlmostEqual(area_pentagon(100), 500.0498948787274)

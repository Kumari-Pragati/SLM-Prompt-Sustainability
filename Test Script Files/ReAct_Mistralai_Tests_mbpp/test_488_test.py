import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(area_pentagon(5), 24.499999999999996, delta=0.000001)

    def test_zero_case(self):
        with self.assertRaises(ValueError):
            area_pentagon(0)

    def test_negative_case(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_large_case(self):
        self.assertAlmostEqual(area_pentagon(100), 100000.00000000001, delta=100000)

    def test_small_case(self):
        self.assertAlmostEqual(area_pentagon(0.1), 0.024499999999999996, delta=0.000001)

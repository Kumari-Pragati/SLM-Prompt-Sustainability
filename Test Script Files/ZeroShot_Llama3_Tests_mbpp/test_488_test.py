import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_area_pentagon_positive(self):
        self.assertAlmostEqual(area_pentagon(1), 0.5396, places=4)

    def test_area_pentagon_negative(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_area_pentagon_zero(self):
        self.assertAlmostEqual(area_pentagon(0), 0.0, places=4)

    def test_area_pentagon_non_numeric(self):
        with self.assertRaises(TypeError):
            area_pentagon('a')

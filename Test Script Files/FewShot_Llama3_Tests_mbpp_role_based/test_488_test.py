import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_positive_side_length(self):
        self.assertAlmostEqual(area_pentagon(5), 12.732051814701357)

    def test_zero_side_length(self):
        with self.assertRaises(ZeroDivisionError):
            area_pentagon(0)

    def test_negative_side_length(self):
        with self.assertRaises(ValueError):
            area_pentagon(-5)

    def test_non_numeric_side_length(self):
        with self.assertRaises(TypeError):
            area_pentagon('five')

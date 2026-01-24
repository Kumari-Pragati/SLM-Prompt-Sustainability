import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(area_pentagon(5), 19.444444444444446)
        self.assertAlmostEqual(area_pentagon(10), 98.55555555555556)

    def test_edge_case_small(self):
        self.assertAlmostEqual(area_pentagon(1), 1.099490243902439)

    def test_edge_case_large(self):
        self.assertAlmostEqual(area_pentagon(100), 9999.999999999999)

    def test_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            area_pentagon(0)

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            area_pentagon('str')

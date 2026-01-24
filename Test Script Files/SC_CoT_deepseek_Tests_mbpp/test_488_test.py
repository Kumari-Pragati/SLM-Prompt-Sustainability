import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(1), 0.589048622547)

    def test_zero_input(self):
        self.assertEqual(area_pentagon(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_large_number(self):
        self.assertAlmostEqual(area_pentagon(10000), 1381966000.0)

    def test_float_input(self):
        self.assertAlmostEqual(area_pentagon(1.5), 1.03353515625)

import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(10), 172.0477341059375)

    def test_zero_input(self):
        self.assertEqual(area_pentagon(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_large_input(self):
        self.assertAlmostEqual(area_pentagon(10000), 17204773410.59375)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            area_pentagon('a')

import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(1), 0.5886034732051607)

    def test_zero_input(self):
        self.assertEqual(area_pentagon(0), 0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            area_pentagon(-1)

    def test_large_input(self):
        self.assertAlmostEqual(area_pentagon(1000), 147745.1629749658)

    def test_edge_case(self):
        self.assertAlmostEqual(area_pentagon(1.4142135623730951), 1.0)

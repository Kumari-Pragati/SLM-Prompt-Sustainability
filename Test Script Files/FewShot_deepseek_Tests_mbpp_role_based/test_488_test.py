import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(area_pentagon(10), 172.0477341059375)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(area_pentagon(0), 0)
        self.assertAlmostEqual(area_pentagon(1), 1.720477341059375)

    def test_edge_conditions(self):
        self.assertAlmostEqual(area_pentagon(1000), 172047.7341059375)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            area_pentagon('a')

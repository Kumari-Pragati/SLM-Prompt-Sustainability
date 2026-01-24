import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_area_pentagon_simple(self):
        self.assertAlmostEqual(area_pentagon(1), 0.589048622547)

    def test_area_pentagon_edge(self):
        self.assertAlmostEqual(area_pentagon(0), 0)
        self.assertAlmostEqual(area_pentagon(1000), 197553.9283908)

    def test_area_pentagon_boundary(self):
        self.assertAlmostEqual(area_pentagon(1.73205080757), 2.0)

    def test_area_pentagon_complex(self):
        self.assertAlmostEqual(area_pentagon(2.0), 3.46410161514)

import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(area_pentagon(3), 9.464101635106416)

    def test_edge_input(self):
        self.assertAlmostEqual(area_pentagon(0), 0)
        self.assertAlmostEqual(area_pentagon(1), 1.5649444594251968)
        self.assertAlmostEqual(area_pentagon(1000), 99999.99999999999)

    def test_complex_input(self):
        self.assertAlmostEqual(area_pentagon(2.5), 13.95348834345777)
        self.assertAlmostEqual(area_pentagon(-3), -27.32425531914813)

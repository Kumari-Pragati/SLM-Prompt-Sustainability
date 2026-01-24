import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(area_pentagon(1), 0.915965594177219)

    def test_edge_case_small(self):
        self.assertAlmostEqual(area_pentagon(0.1), 0.00915965594177219)

    def test_edge_case_large(self):
        self.assertAlmostEqual(area_pentagon(100), 915.965594177219)

    def test_boundary_case_zero(self):
        self.assertAlmostEqual(area_pentagon(0), 0.0)

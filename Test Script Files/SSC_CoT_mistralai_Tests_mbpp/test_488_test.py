import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(area_pentagon(1), 0.61803398875, delta=0.0001)
        self.assertAlmostEqual(area_pentagon(2), 1.2360679775, delta=0.0001)
        self.assertAlmostEqual(area_pentagon(3), 1.8530988673, delta=0.0001)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(area_pentagon(0), 0, delta=0.0001)
        self.assertAlmostEqual(area_pentagon(1e-5), 0.61803398875, delta=0.0001)
        self.assertAlmostEqual(area_pentagon(1e6), 1884955592153.9898, delta=1e6)

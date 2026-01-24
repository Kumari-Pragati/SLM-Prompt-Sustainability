import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(perimeter_pentagon(5), 25)
        self.assertAlmostEqual(perimeter_pentagon(10), 50)
        self.assertAlmostEqual(perimeter_pentagon(15), 75)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(perimeter_pentagon(0), 0)
        self.assertAlmostEqual(perimeter_pentagon(1), 5)

    def test_corner_cases(self):
        self.assertAlmostEqual(perimeter_pentagon(100), 500)
        self.assertAlmostEqual(perimeter_pentagon(0.5), 2.5)

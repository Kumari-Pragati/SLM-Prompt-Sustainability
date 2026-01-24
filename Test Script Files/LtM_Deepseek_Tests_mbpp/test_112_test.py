import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(perimeter(10, 5), 30)
        self.assertAlmostEqual(perimeter(20, 10), 60)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(perimeter(0, 0), 0)
        self.assertAlmostEqual(perimeter(1, 1), 4)
        self.assertAlmostEqual(perimeter(1000, 500), 3000)

    def test_edge_conditions(self):
        self.assertAlmostEqual(perimeter(float('inf'), float('inf')), float('inf'))
        self.assertAlmostEqual(perimeter(-10, -5), -10)
        self.assertAlmostEqual(perimeter(float('-inf'), float('-inf')), float('-inf'))

    def test_complex_cases(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8)
        self.assertAlmostEqual(perimeter(100, 50), 300)

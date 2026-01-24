import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon_simple(self):
        self.assertEqual(perimeter_pentagon(5), 25)
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_perimeter_pentagon_edge(self):
        self.assertEqual(perimeter_pentagon(0), 0)
        self.assertEqual(perimeter_pentagon(1), 5)

    def test_perimeter_pentagon_boundary(self):
        self.assertEqual(perimeter_pentagon(10000), 50000)
        self.assertEqual(perimeter_pentagon(float('inf')), float('inf'))

    def test_perimeter_pentagon_complex(self):
        self.assertEqual(perimeter_pentagon(0.5), 2.5)
        self.assertEqual(perimeter_pentagon(-5), -25)

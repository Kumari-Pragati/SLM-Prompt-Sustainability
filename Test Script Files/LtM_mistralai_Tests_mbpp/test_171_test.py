import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(perimeter_pentagon(3), 15)

    def test_edge_input(self):
        self.assertEqual(perimeter_pentagon(0), 0)
        self.assertEqual(perimeter_pentagon(1), 5)

    def test_boundary_input(self):
        self.assertEqual(perimeter_pentagon(math.pi), round(perimeter_pentagon(math.pi), 2))
        self.assertEqual(perimeter_pentagon(math.e), round(perimeter_pentagon(math.e), 2))

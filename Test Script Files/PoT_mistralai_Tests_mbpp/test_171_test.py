import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(perimeter_pentagon(3), 15)

    def test_edge_case_small(self):
        self.assertEqual(perimeter_pentagon(1), 5)

    def test_edge_case_large(self):
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_boundary_case_zero(self):
        self.assertEqual(perimeter_pentagon(0), 0)

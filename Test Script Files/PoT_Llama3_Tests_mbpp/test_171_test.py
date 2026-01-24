import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_edge_case_zero(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('a')

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(5.5)

    def test_edge_case_large(self):
        self.assertEqual(perimeter_pentagon(1000), 5000)

    def test_edge_case_small(self):
        self.assertEqual(perimeter_pentagon(0.5), 2.5)

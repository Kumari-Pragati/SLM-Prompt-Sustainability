import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_boundary_condition(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_edge_condition(self):
        self.assertEqual(perimeter_pentagon(100), 500)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('a')

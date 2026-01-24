import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(90, 90, 100))

    def test_edge_case_triangle(self):
        self.assertTrue(validity_triangle(90, 90, 0))

    def test_edge_case_triangle2(self):
        self.assertFalse(validity_triangle(90, 90, 90))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            validity_triangle('a', 'b', 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            validity_triangle(-1, 1, 1)

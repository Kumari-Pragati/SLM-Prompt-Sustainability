import unittest
from mbpp_677_code import validity_triangle

class TestValidityTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertTrue(validity_triangle(60, 60, 60))

    def test_invalid_triangle(self):
        self.assertFalse(validity_triangle(90, 90, 90))

    def test_edge_case_triangle(self):
        self.assertTrue(validity_triangle(90, 30, 60))

    def test_edge_case_invalid_triangle(self):
        self.assertFalse(validity_triangle(90, 90, 100))

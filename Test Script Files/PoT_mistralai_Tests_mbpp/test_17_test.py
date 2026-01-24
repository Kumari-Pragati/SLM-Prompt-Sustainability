import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(square_perimeter(3), 12)

    def test_edge_case_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_edge_case_negative(self):
        self.assertEqual(square_perimeter(-1), None)

    def test_boundary_case_small(self):
        self.assertEqual(square_perimeter(1.5), 6)

    def test_boundary_case_large(self.test_typical_case)

import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_edge_case_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            square_perimeter(-1)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')

    def test_edge_case_zero_input(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_edge_case_positive(self):
        self.assertEqual(square_perimeter(10), 40)

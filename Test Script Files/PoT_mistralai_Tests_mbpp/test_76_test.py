import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 5), 14)
        self.assertEqual(count_Squares(5, 7), 21)
        self.assertEqual(count_Squares(7, 9), 36)

    def test_edge_case_equal_dimensions(self):
        self.assertEqual(count_Squares(2, 2), 4)
        self.assertEqual(count_Squares(4, 4), 40)

    def test_edge_case_one_dimension(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(0, 0), 0)

    def test_corner_case_one_dimension_zero(self):
        self.assertEqual(count_Squares(0, 1), 1)

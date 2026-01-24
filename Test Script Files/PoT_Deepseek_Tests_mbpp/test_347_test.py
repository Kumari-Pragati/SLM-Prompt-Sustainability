import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Squares(2, 3), 6)
        self.assertEqual(count_Squares(5, 5), 25)
        self.assertEqual(count_Squares(1, 1), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Squares(0, 5), 0)
        self.assertEqual(count_Squares(5, 0), 0)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 1000), 1000)
        self.assertEqual(count_Squares(1000, 1), 1000)

    def test_corner_cases(self):
        self.assertEqual(count_Squares(2, 2), 4)
        self.assertEqual(count_Squares(3, 3), 9)
        self.assertEqual(count_Squares(4, 4), 16)

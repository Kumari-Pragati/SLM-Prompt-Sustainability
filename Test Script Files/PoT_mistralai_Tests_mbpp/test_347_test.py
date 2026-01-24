import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 4), 14)
        self.assertEqual(count_Squares(4, 5), 21)
        self.assertEqual(count_Squares(5, 6), 30)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(count_Squares(1, 2), 6)
        self.assertEqual(count_Squares(2, 1), 6)
        self.assertEqual(count_Squares(100, 100), 338350)

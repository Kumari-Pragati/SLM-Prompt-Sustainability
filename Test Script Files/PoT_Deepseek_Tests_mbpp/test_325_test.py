import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(4), 1)
        self.assertEqual(get_Min_Squares(9), 1)
        self.assertEqual(get_Min_Squares(12), 2)
        self.assertEqual(get_Min_Squares(13), 2)
        self.assertEqual(get_Min_Squares(16), 1)
        self.assertEqual(get_Min_Squares(17), 2)
        self.assertEqual(get_Min_Squares(20), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(4), 1)

    def test_corner_cases(self):
        self.assertEqual(get_Min_Squares(5), 2)
        self.assertEqual(get_Min_Squares(6), 2)
        self.assertEqual(get_Min_Squares(7), 3)
        self.assertEqual(get_Min_Squares(8), 2)
        self.assertEqual(get_Min_Squares(9), 1)
        self.assertEqual(get_Min_Squares(10), 2)
        self.assertEqual(get_Min_Squares(11), 2)
        self.assertEqual(get_Min_Squares(12), 2)

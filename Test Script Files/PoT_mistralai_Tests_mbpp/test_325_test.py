import unittest
from325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(9), 3)
        self.assertEqual(get_Min_Squares(16), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(10), 4)
        self.assertEqual(get_Min_Squares(20), 5)
        self.assertEqual(get_Min_Squares(27), 6)

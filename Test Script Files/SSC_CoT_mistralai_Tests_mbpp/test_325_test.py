import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(9), 3)
        self.assertEqual(get_Min_Squares(25), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(49), 7)
        self.assertEqual(get_Min_Squares(100), 10)

    def test_special_cases(self):
        self.assertEqual(get_Min_Squares(5), 2)
        self.assertEqual(get_Min_Squares(10), 3)
        self.assertEqual(get_Min_Squares(20), 4)
        self.assertEqual(get_Min_Squares(40), 5)
        self.assertEqual(get_Min_Squares(625), 16)

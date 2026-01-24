import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(5), 3)
        self.assertEqual(get_Min_Squares(6), 3)

    def test_edge_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(5), 3)
        self.assertEqual(get_Min_Squares(6), 3)

    def test_complex_inputs(self):
        self.assertEqual(get_Min_Squares(7), 2)
        self.assertEqual(get_Min_Squares(8), 2)
        self.assertEqual(get_Min_Squares(9), 3)
        self.assertEqual(get_Min_Squares(10), 2)
        self.assertEqual(get_Min_Squares(11), 3)
        self.assertEqual(get_Min_Squares(12), 3)

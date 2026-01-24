import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(4), 4)
        self.assertEqual(get_Min_Squares(5), 5)
        self.assertEqual(get_Min_Squares(6), 3)
        self.assertEqual(get_Min_Squares(7), 4)
        self.assertEqual(get_Min_Squares(8), 5)
        self.assertEqual(get_Min_Squares(9), 3 + get_Min_Squares(7))

    def test_complex_inputs(self):
        self.assertEqual(get_Min_Squares(10), 4)
        self.assertEqual(get_Min_Squares(11), 4)
        self.assertEqual(get_Min_Squares(12), 5)
        self.assertEqual(get_Min_Squares(13), 4)
        self.assertEqual(get_Min_Squares(14), 5)
        self.assertEqual(get_Min_Squares(15), 4)
        self.assertEqual(get_Min_Squares(16), 5)
        self.assertEqual(get_Min_Squares(17), 4)
        self.assertEqual(get_Min_Squares(18), 5)
        self.assertEqual(get_Min_Squares(19), 6)

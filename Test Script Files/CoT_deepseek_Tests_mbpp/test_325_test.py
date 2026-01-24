import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_get_Min_Squares_typical_cases(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(4), 1)
        self.assertEqual(get_Min_Squares(9), 1)
        self.assertEqual(get_Min_Squares(12), 2)
        self.assertEqual(get_Min_Squares(13), 2)
        self.assertEqual(get_Min_Squares(16), 1)
        self.assertEqual(get_Min_Squares(17), 2)
        self.assertEqual(get_Min_Squares(20), 2)

    def test_get_Min_Squares_edge_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(3), 3)

    def test_get_Min_Squares_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Min_Squares('a')
        with self.assertRaises(TypeError):
            get_Min_Squares(None)
        with self.assertRaises(TypeError):
            get_Min_Squares([1, 2, 3])

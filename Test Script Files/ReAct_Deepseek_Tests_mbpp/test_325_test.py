import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(4), 4)
        self.assertEqual(get_Min_Squares(9), 1)
        self.assertEqual(get_Min_Squares(16), 1)
        self.assertEqual(get_Min_Squares(17), 2)
        self.assertEqual(get_Min_Squares(20), 2)
        self.assertEqual(get_Min_Squares(325), 1)

    def test_edge_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(4), 4)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            get_Min_Squares('a')
        with self.assertRaises(TypeError):
            get_Min_Squares(None)
        with self.assertRaises(TypeError):
            get_Min_Squares([1, 2, 3])
        with self.assertRaises(ValueError):
            get_Min_Squares(-5)

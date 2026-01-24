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
        self.assertEqual(get_Min_Squares(21), 2)
        self.assertEqual(get_Min_Squares(25), 1)

    def test_edge_cases(self):
        self.assertEqual(get_Min_Squares(0), 0)
        self.assertEqual(get_Min_Squares(1), 1)
        self.assertEqual(get_Min_Squares(2), 2)
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(4), 1)

    def test_corner_cases(self):
        self.assertEqual(get_Min_Squares(100), 1)
        self.assertEqual(get_Min_Squares(101), 2)
        self.assertEqual(get_Min_Squares(102), 2)
        self.assertEqual(get_Min_Squares(103), 2)
        self.assertEqual(get_Min_Squares(104), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Min_Squares("10")
        with self.assertRaises(TypeError):
            get_Min_Squares(None)
        with self.assertRaises(TypeError):
            get_Min_Squares([10])
        with self.assertRaises(TypeError):
            get_Min_Squares({10})

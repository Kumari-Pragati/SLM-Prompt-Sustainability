import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 2)
        self.assertEqual(count_Odd_Squares(10, 100), 5)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, -1), 0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares("1", 25)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, "25")
        with self.assertRaises(TypeError):
            count_Odd_Squares("1", "25")

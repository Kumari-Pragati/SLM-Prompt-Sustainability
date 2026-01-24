import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(3, 3), 18)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 2), 6)
        self.assertEqual(count_Squares(2, 1), 2)
        self.assertEqual(count_Squares(100, 100), 338350)

    def test_complex(self):
        self.assertEqual(count_Squares(1, 100), 1475)
        self.assertEqual(count_Squares(100, 1), 1475)
        self.assertEqual(count_Squares(10, 20), 920)
        self.assertEqual(count_Squares(20, 10), 920)

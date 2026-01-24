import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 3)
        self.assertEqual(count_Squares(3, 3), 6)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Squares(0, 1), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(1, 2147483647), 2147483647)
        self.assertEqual(count_Squares(2147483647, 1), 2147483647)

    def test_complex(self):
        self.assertEqual(count_Squares(1, 100), 338)
        self.assertEqual(count_Squares(100, 1), 338)
        self.assertEqual(count_Squares(1000, 1000), 338338)

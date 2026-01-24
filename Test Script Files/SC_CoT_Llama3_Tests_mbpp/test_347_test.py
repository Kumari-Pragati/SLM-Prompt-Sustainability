import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Squares(2, 3), 14)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(1, 2), 3)
        self.assertEqual(count_Squares(2, 1), 3)
        self.assertEqual(count_Squares(2, 2), 6)

    def test_boundary_cases(self):
        self.assertEqual(count_Squares(3, 3), 28)
        self.assertEqual(count_Squares(4, 4), 70)

    def test_special_cases(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares('a', 2)
        with self.assertRaises(TypeError):
            count_Squares(2, 'b')

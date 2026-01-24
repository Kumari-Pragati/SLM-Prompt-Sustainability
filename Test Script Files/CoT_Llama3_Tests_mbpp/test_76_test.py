import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(count_Squares(3, 4), 30)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(3, 3), 36)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares('a', 4)
        with self.assertRaises(TypeError):
            count_Squares(3, 'b')

    def test_boundary_conditions(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 1), 0)

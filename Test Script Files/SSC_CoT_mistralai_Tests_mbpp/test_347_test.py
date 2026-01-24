import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Squares(3, 4), 18)
        self.assertEqual(count_Squares(4, 4), 10)
        self.assertEqual(count_Squares(5, 5), 25)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 0), 1)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 1), 2)
        self.assertEqual(count_Squares(1, 2), 2)
        self.assertEqual(count_Squares(1, 0), 1)
        self.assertEqual(count_Squares(0, 2), 2)
        self.assertEqual(count_Squares(2, 2), 10)
        self.assertEqual(count_Squares(3, 1), 6)
        self.assertEqual(count_Squares(1, 3), 6)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            count_Squares(-1, 2)
        with self.assertRaises(ValueError):
            count_Squares(2, -1)

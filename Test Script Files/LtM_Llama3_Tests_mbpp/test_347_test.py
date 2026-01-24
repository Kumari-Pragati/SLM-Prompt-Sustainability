import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(3, 3), 16)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 0), 0)
        self.assertEqual(count_Squares(0, 1), 0)
        self.assertEqual(count_Squares(2, 1), 2)
        self.assertEqual(count_Squares(1, 2), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares('a', 1)
        with self.assertRaises(TypeError):
            count_Squares(1, 'b')

import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(next_Perfect_Square(1), 4)
        self.assertEqual(next_Perfect_Square(4), 9)
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_case(self):
        self.assertEqual(next_Perfect_Square(0), 1)
        self.assertEqual(next_Perfect_Square(1), 4)

    def test_corner_case(self):
        self.assertEqual(next_Perfect_Square(8), 9)
        self.assertEqual(next_Perfect_Square(9), 16)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square("abc")
        with self.assertRaises(TypeError):
            next_Perfect_Square(None)
        with self.assertRaises(TypeError):
            next_Perfect_Square([1,2,3])

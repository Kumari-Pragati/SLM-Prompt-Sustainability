import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(next_Perfect_Square(16), 25)
        self.assertEqual(next_Perfect_Square(25), 25)
        self.assertEqual(next_Perfect_Square(36), 49)

    def test_edge_cases(self):
        self.assertEqual(next_Perfect_Square(0), 0)
        self.assertEqual(next_Perfect_Square(1), 1)
        self.assertEqual(next_Perfect_Square(4), 5)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            next_Perfect_Square(-1)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square(3.5)

    def test_large_inputs(self):
        self.assertEqual(next_Perfect_Square(1000000), 1000001)

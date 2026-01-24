import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_case(self):
        self.assertEqual(next_Perfect_Square(0), 1)

    def test_boundary_case(self):
        self.assertEqual(next_Perfect_Square(81), 100)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square('abc')

import unittest
from mbpp_244_code import next_Perfect_Square

class TestNextPerfectSquare(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(next_Perfect_Square(16), 25)

    def test_edge_case_N_0(self):
        self.assertEqual(next_Perfect_Square(0), 0)

    def test_edge_case_N_1(self):
        self.assertEqual(next_Perfect_Square(1), 1)

    def test_edge_case_N_negative(self):
        with self.assertRaises(ValueError):
            next_Perfect_Square(-1)

    def test_edge_case_N_non_integer(self):
        with self.assertRaises(TypeError):
            next_Perfect_Square(3.14)

    def test_edge_case_N_large(self):
        self.assertEqual(next_Perfect_Square(1000000), 1000001)

import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(dig_let('a1b2c3'), (3, 3))

    def test_edge_condition(self):
        self.assertEqual(dig_let(''), (0, 0))

    def test_boundary_condition(self):
        self.assertEqual(dig_let('1234567890'), (0, 10))
        self.assertEqual(dig_let('abcdefghijklmnopqrstuvwxyz'), (26, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dig_let(12345)

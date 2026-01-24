import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(even_num(4))

    def test_edge_case(self):
        self.assertTrue(even_num(0))

    def test_boundary_case(self):
        self.assertFalse(even_num(1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            even_num('a')

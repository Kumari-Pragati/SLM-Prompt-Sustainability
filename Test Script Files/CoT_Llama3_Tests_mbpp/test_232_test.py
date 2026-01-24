import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [9, 8, 7])

    def test_edge_case(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [10])

    def test_edge_case2(self):
        self.assertEqual(larg_nnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            larg_nnum("hello", 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            larg_nnum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "hello")

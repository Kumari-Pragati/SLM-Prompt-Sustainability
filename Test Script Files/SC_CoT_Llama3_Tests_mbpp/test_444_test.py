import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 1), '[(2, 3), (5, 6)]')

    def test_edge_case(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 0), '[(1, 2, 3), (4, 5, 6)]')

    def test_edge_case2(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 2), '[(1, 2), (5, 6)]')

    def test_edge_case3(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 3), '[(1, 2, 3), ()]')

    def test_edge_case4(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 4), '[(1, 2, 3), ()]')

    def test_edge_case5(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 5), '[(1, 2, 3), ()]')

    def test_edge_case6(self):
        self.assertEqual(trim_tuple([(1, 2, 3), (4, 5, 6)], 6), '[(1, 2, 3), ()]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            trim_tuple(None, 1)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            trim_tuple([], 1)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            trim_tuple([(1, 2, 3)], 'a')

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            trim_tuple([(1, 2, 3)], 1.5)

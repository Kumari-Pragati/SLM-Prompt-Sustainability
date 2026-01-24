import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_normal(self):
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b, c)), [(1, a), (2, b), (3, c)])
        self.assertListEqual(zip_tuples((1, 2, 3, 4), (a, b, c)), [(1, a), (2, b), (3, c), (4, None)])

    def test_edge_and_boundary(self):
        self.assertListEqual(zip_tuples((1, 2), (a, b, c)), [(1, a), (2, b)])
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b)), [(1, a), (2, b), (3, None)])
        self.assertListEqual(zip_tuples((1, 2, 3), ()), [(1, None), (2, None), (3, None)])
        self.assertListEqual(zip_tuples((1, 2, 3), (a, b, c, d)), [(1, a), (2, b), (3, c)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, zip_tuples, (1, 2), 3)
        self.assertRaises(TypeError, zip_tuples, [1, 2], [3, 4, 5])

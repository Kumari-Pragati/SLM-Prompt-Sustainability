import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), "1-2-3")

    def test_edge_cases(self):
        self.assertEqual(concatenate_tuple(()), "")
        self.assertEqual(concatenate_tuple((1,)), "1")
        self.assertEqual(concatenate_tuple((1, 2)), "1-2")
        self.assertEqual(concatenate_tuple((1, 2, 1)), "1-2-1")

    def test_boundary_cases(self):
        self.assertEqual(concatenate_tuple((-1, 0, 1)), "-1-0-1")
        self.assertEqual(concatenate_tuple((1, -1, 0)), "1-0-1-")
        self.assertEqual(concatenate_tuple((1, 2, -1)), "1-2-1-")

    def test_invalid_input(self):
        self.assertRaises(TypeError, concatenate_tuple, (1.5, 2))
        self.assertRaises(TypeError, concatenate_tuple, ([1, 2, 3]))

import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(super_seq([1, 2, 3], [2, 3, 4], 3, 3), 1)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 3, 3), 0)
        self.assertEqual(super_seq([1, 2, 3], [4, 5, 6], 3, 3), 3)

    def test_edge_cases(self):
        self.assertEqual(super_seq([1, 2, 3], [2, 3], 3, 2), 1)
        self.assertEqual(super_seq([1, 2, 3], [2, 3, 4, 5], 3, 4), 2)
        self.assertEqual(super_seq([1, 2], [1, 2, 3], 2, 3, ), 1)

    def test_special_cases(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 0, 3), 0)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 3, 0), 0)
        self.assertEqual(super_seq([], [1, 2, 3], 0, 3), 3)
        self.assertEqual(super_seq([1, 2, 3], [], 3, 0), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            super_seq('a', [1, 2, 3], 3, 3)
        with self.assertRaises(TypeError):
            super_seq([1, 2, 3], 'a', 3, 3)
        with self.assertRaises(TypeError):
            super_seq([1, 2, 3], [1, 2, 3], 'a', 3)
        with self.assertRaises(TypeError):
            super_seq([1, 2, 3], [1, 2, 3], 3, 'a')

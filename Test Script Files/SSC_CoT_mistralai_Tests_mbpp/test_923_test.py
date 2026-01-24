import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 3, 3), 4)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 3, 2), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 2, 3), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 2, 2), 1)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 1, 3), 2)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 1, 2), 1)

    def test_edge_cases(self):
        self.assertEqual(super_seq([], [], 0, 0), 0)
        self.assertEqual(super_seq([1], [], 0, 0), 1)
        self.assertEqual(super_seq([], [1], 0, 0), 1)
        self.assertEqual(super_seq([1], [1], 0, 0), 1)

        self.assertEqual(super_seq([1, 2, 3, 4], [], 3, 0), 3)
        self.assertEqual(super_seq([], [1, 2, 3, 4], 0, 3), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [1, 2, 3, 4], 0, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 0, 3), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 4, 0), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], -1, 3), None)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 9, 8, 7], 3, -1), None)

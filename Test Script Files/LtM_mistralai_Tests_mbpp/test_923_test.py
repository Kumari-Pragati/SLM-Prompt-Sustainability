import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_simple_equal(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 2, 2), 3)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 1, 1), 1)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 0, 0), 0)

    def test_simple_not_equal(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 2, 2), 2)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 1, 1), 1)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(super_seq([], [], 0, 0), 0)
        self.assertEqual(super_seq([1], [], 0, 0), 0)
        self.assertEqual(super_seq([], [1], 0, 0), 0)
        self.assertEqual(super_seq([1], [1], 0, 0), 0)

        self.assertEqual(super_seq([1, 2, 3], [], 2, 0), 2)
        self.assertEqual(super_seq([], [1, 2, 3], 0, 2), 2)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3, 4], 3, 3), 4)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 4, 4), 4)

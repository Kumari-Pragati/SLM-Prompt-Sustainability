import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 3, 3), 1)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 2, 3), 2)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 1, 3), 3)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 3, 2), 2)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 2, 2), 1)
        self.assertEqual(super_seq([1, 2, 3, 4], [10, 20, 30, 40], 1, 1), 0)

    def test_edge_case_empty_input(self):
        self.assertEqual(super_seq([], [], 0, 0), 0)
        self.assertEqual(super_seq([], [], 0, 1), 1)
        self.assertEqual(super_seq([], [], 1, 0), 1)

    def test_edge_case_single_input(self):
        self.assertEqual(super_seq([1], [], 0, 0), 1)
        self.assertEqual(super_seq([], [1], 0, 0), 1)

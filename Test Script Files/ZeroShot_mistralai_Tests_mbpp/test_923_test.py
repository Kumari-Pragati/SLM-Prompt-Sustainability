import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_empty_sequences(self):
        self.assertEqual(super_seq([], [], 0, 0), 0)
        self.assertEqual(super_seq([], [1], 0, 1), 1)
        self.assertEqual(super_seq([1], [], 1, 0), 1)

    def test_single_element_sequences(self):
        self.assertEqual(super_seq([1], [1], 0, 1), 1)
        self.assertEqual(super_seq([1], [2], 0, 1), 2)
        self.assertEqual(super_seq([2], [1], 0, 1), 2)

    def test_equal_sequences(self):
        self.assertEqual(super_seq([1, 1], [1, 1], 1, 1), 2)
        self.assertEqual(super_seq([1, 2, 1], [1, 2, 1], 2, 2), 3)
        self.assertEqual(super_seq([1, 2, 3, 1], [1, 2, 3, 1], 3, 3), 4)

    def test_inequal_sequences(self):
        self.assertEqual(super_seq([1, 1], [2, 1], 1, 1), 2)
        self.assertEqual(super_seq([1, 2, 1], [1, 2, 3], 2, 2), 3)
        self.assertEqual(super_seq([1, 2, 3, 1], [1, 2, 4], 3, 3), 4)

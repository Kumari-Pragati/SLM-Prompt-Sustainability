import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_empty_sequences(self):
        self.assertEqual(super_seq( [], [], 0, 0 ), 0)
        self.assertEqual(super_seq( [], [], 1, 0 ), 1)
        self.assertEqual(super_seq( [], [], 0, 1 ), 1)

    def test_single_element_sequences(self):
        self.assertEqual(super_seq([1], [1], 0, 0 ), 1)
        self.assertEqual(super_seq([1], [2], 0, 0 ), 0)
        self.assertEqual(super_seq([1], [], 0, 0 ), 0)

    def test_equal_elements(self):
        self.assertEqual(super_seq([1, 1], [1, 1], 1, 1 ), 2)
        self.assertEqual(super_seq([1, 2, 1], [1, 2, 1], 2, 2 ), 3)
        self.assertEqual(super_seq([1, 2, 3, 1], [1, 2, 3, 1], 3, 3 ), 4)

    def test_different_elements(self):
        self.assertEqual(super_seq([1, 2], [1, 3], 1, 1 ), 1)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 2, 2 ), 2)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 3, 2 ), 3)
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 2, 3 ), 3)

    def test_negative_indices(self):
        self.assertRaises(IndexError, lambda: super_seq([1], [1], -1, 0))
        self.assertRaises(IndexError, lambda: super_seq([1], [1], 0, -1))
        self.assertRaises(IndexError, lambda: super_seq([1], [1], -1, -1))

    def test_out_of_range_indices(self):
        self.assertEqual(super_seq([1, 2], [1, 2], 2, 2 ), 1)
        self.assertEqual(super_seq([1, 2], [1, 2], 3, 2 ), 1)
        self.assertEqual(super_seq([1, 2], [1, 2], 2, 3 ), 1)
        self.assertEqual(super_seq([1, 2], [1, 2], 3, 3 ), 1)

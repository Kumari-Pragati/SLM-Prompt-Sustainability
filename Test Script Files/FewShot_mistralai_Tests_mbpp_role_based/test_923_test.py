import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_empty_sequences(self):
        self.assertEqual(super_seq( [], [], 0, 0 ), 0)

    def test_single_element_sequences(self):
        self.assertEqual(super_seq( [1], [], 0, 0 ), 0)
        self.assertEqual(super_seq( [], [1], 0, 0 ), 0)
        self.assertEqual(super_seq( [1], [1], 0, 0 ), 1)

    def test_equal_sequences(self):
        self.assertEqual(super_seq( [1, 2, 3], [1, 2, 3], 2, 2 ), 3)

    def test_different_lengths(self):
        self.assertEqual(super_seq( [1, 2, 3], [1, 2], 2, 1 ), 1)
        self.assertEqual(super_seq( [1, 2], [1, 2, 3], 1, 2 ), 1)

    def test_different_elements(self):
        self.assertEqual(super_seq( [1, 2, 3], [4, 5, 6], 2, 2 ), 1)

    def test_negative_indices(self):
        self.assertRaises(IndexError, lambda: super_seq( [1, 2, 3], [4, 5, 6], -1, 0 ))
        self.assertRaises(IndexError, lambda: super_seq( [1, 2, 3], [4, 5, 6], 0, -1 ))

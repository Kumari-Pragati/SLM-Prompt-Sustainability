import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 3), [2, 3, 4, 5, 1])

    def test_edge_case_start(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 3), [1, 2, 3, 4, 5])

    def test_edge_case_end(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 5), [3, 4, 5, 1, 2])

    def test_edge_case_rotate_full(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_zero(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_rotate_full_reverse_reverse
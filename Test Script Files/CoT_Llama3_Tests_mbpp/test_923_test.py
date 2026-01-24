import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_empty_m(self):
        self.assertEqual(super_seq([], [1, 2, 3], 0, 3), 3)

    def test_empty_n(self):
        self.assertEqual(super_seq([1, 2, 3], [], 3, 0), 3)

    def test_match(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 3, 3), 1)

    def test_no_match(self):
        self.assertEqual(super_seq([1, 2, 3], [4, 5, 6], 3, 3), 3)

    def test_m_n_equal(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 2, 2), 1)

    def test_m_n_diff(self):
        self.assertEqual(super_seq([1, 2, 3], [4, 5, 6], 2, 3), 3)

    def test_m_zero(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 0, 3), 3)

    def test_n_zero(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 3, 0), 3)

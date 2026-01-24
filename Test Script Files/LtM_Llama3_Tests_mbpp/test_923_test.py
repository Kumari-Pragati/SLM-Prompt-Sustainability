import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_empty_m(self):
        self.assertEqual(super_seq([], [1, 2, 3], 0, 3), 3)

    def test_empty_n(self):
        self.assertEqual(super_seq([1, 2, 3], [], 3, 0), 3)

    def test_m_n_equal(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 3], 3, 3), 3)

    def test_m_n_not_equal(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2, 4], 3, 4), 1)

    def test_m_greater_n(self):
        self.assertEqual(super_seq([1, 2, 3], [1, 2], 3, 2), 1)

    def test_n_greater_m(self):
        self.assertEqual(super_seq([1, 2], [1, 2, 3], 2, 3), 1)

    def test_m_zero(self):
        self.assertEqual(super_seq([], [1, 2, 3], 0, 3), 3)

    def test_n_zero(self):
        self.assertEqual(super_seq([1, 2, 3], [], 3, 0), 3)

    def test_m_one(self):
        self.assertEqual(super_seq([1], [1, 2, 3], 1, 3), 2)

    def test_n_one(self):
        self.assertEqual(super_seq([1, 2, 3], [1], 3, 1), 2)

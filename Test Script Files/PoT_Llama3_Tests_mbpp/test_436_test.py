import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_typical_positive(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_typical_negative(self):
        self.assertEqual(-5, neg_nos([-5]))

    def test_typical_mixed(self):
        self.assertIsNone(neg_nos([1, -2, 3]))

    def test_edge_empty(self):
        self.assertIsNone(neg_nos([]))

    def test_edge_single_positive(self):
        self.assertIsNone(neg_nos([1]))

    def test_edge_single_negative(self):
        self.assertEqual(-1, neg_nos([-1]))

    def test_edge_single_zero(self):
        self.assertIsNone(neg_nos([0]))

    def test_edge_single_non_numeric(self):
        with self.assertRaises(TypeError):
            neg_nos(['a'])

    def test_edge_multiple_non_numeric(self):
        with self.assertRaises(TypeError):
            neg_nos([1, 'a', 3])

import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_typical_positive(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_typical_negative(self):
        with self.assertRaises(TypeError):
            pos_nos([-1, -2, -3])

    def test_typical_mixed(self):
        with self.assertRaises(TypeError):
            pos_nos([-1, 2, -3])

    def test_edge_zero(self):
        self.assertEqual(pos_nos([0]), 0)

    def test_edge_negative(self):
        with self.assertRaises(TypeError):
            pos_nos([-1])

    def test_edge_positive(self):
        self.assertEqual(pos_nos([1]), 1)

    def test_corner_empty(self):
        with self.assertRaises(IndexError):
            pos_nos([])

    def test_corner_single(self):
        self.assertEqual(pos_nos([1]), 1)

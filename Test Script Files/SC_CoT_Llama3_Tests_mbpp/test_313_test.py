import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_typical_positive(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_typical_negative(self):
        self.assertIsNone(pos_nos([-1, -2, -3]))

    def test_typical_mixed(self):
        self.assertIsNone(pos_nos([-1, 2, -3]))

    def test_edge_positive(self):
        self.assertEqual(pos_nos([0]), 0)

    def test_edge_zero(self):
        self.assertEqual(pos_nos([0, 1, 2]), 0)

    def test_edge_negative(self):
        self.assertIsNone(pos_nos([-1, -2, 0]))

    def test_edge_mixed(self):
        self.assertIsNone(pos_nos([-1, 0, -2]))

    def test_special_empty(self):
        self.assertIsNone(pos_nos([]))

    def test_special_single(self):
        self.assertEqual(pos_nos([1]), 1)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            pos_nos("not a list")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            pos_nos(123)

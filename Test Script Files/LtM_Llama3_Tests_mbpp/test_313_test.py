import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(pos_nos([1]), 1)

    def test_simple_zero(self):
        self.assertEqual(pos_nos([0]), 0)

    def test_simple_negative(self):
        with self.assertRaises(TypeError):
            pos_nos([-1])

    def test_empty_list(self):
        with self.assertRaises(TypeError):
            pos_nos([])

    def test_list_of_positives(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_list_of_zeros(self):
        self.assertEqual(pos_nos([0, 0, 0]), 0)

    def test_list_of_pos_and_neg(self):
        with self.assertRaises(TypeError):
            pos_nos([1, -1])

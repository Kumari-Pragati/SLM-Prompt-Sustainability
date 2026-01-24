import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(pos_nos([1, 2, 3]), [1, 2, 3])

    def test_single_positive(self):
        self.assertEqual(pos_nos([5]), 5)

    def test_empty_list(self):
        self.assertEqual(pos_nos([]), [])

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3]), [])

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([1, -2, 3, -4, 5]), [1, 3, 5])

    def test_max_int_value(self):
        self.assertEqual(pos_nos([2147483647]), [2147483647])

    def test_min_int_value(self):
        self.assertEqual(pos_nos([-2147483648]), [])

import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(pos_nos([-1, 2, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3]), None)

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([-1, 0, 2]), 0)

    def test_empty_list(self):
        self.assertEqual(pos_nos([]), None)

    def test_all_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_all_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3]), None)

    def test_zero(self):
        self.assertEqual(pos_nos([-1, 0, 2]), 0)

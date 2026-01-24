import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_multiple_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, 4]), 1)

    def test_zero(self):
        self.assertEqual(pos_nos([0, 1, 2]), 0)

    def test_negative_numbers(self):
        self.assertIsNone(pos_nos([-1, -2, -3]))

    def test_empty_list(self):
        self.assertIsNone(pos_nos([]))

    def test_mixed_list(self):
        self.assertEqual(pos_nos([-1, 0, 1]), 0)

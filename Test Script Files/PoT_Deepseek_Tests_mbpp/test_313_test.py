import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(pos_nos([-1, -2, 3, 4]), 3)

    def test_empty_list(self):
        self.assertIsNone(pos_nos([]))

    def test_all_negative_numbers(self):
        self.assertIsNone(pos_nos([-1, -2, -3]))

    def test_all_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([-1, -2, 0, -3]), 0)

    def test_single_negative_number(self):
        self.assertIsNone(pos_nos([-1]))

    def test_single_positive_number(self):
        self.assertEqual(pos_nos([1]), 1)

    def test_zero(self):
        self.assertEqual(pos_nos([0]), 0)

import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([-1, 2, 3, 4]), 2)
        self.assertEqual(pos_nos([0, -1, -2, 3]), 0)
        self.assertEqual(pos_nos([-5, -4, -3, 0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3, -4]), -1)
        self.assertEqual(pos_nos([-9, -8, -7, -6]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([-1, 0, 2, -3]), 0)
        self.assertEqual(pos_nos([-5, 0, 5, -10]), 0)

    def test_empty_list(self):
        self.assertIsNone(pos_nos([]))

    def test_all_negative(self):
        self.assertIsNone(pos_nos([-1, -2, -3]))

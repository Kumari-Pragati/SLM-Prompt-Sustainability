import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([-1, 2, 3, 4]), 2)
        self.assertEqual(pos_nos([-5, 0, 10, 15]), 0)
        self.assertEqual(pos_nos([-10, -20, 30, 40]), 30)

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3, -4]), -1)
        self.assertEqual(pos_nos([-5, -10, -15, -20]), -5)

    def test_mixed_numbers(self):
        self.assertEqual(pos_nos([-1, 0, 1, -2]), 0)
        self.assertEqual(pos_nos([-5, -4, 0, 1]), 0)

    def test_empty_list(self):
        self.assertIsNone(pos_nos([]))

    def test_all_negative(self):
        self.assertIsNone(pos_nos([-1, -2, -3]))

    def test_all_positive(self):
        self.assertEqual(pos_nos([1, 2, 3]), 1)

    def test_mixed_positive_negative(self):
        self.assertEqual(pos_nos([-1, 2, -3, 4]), 2)

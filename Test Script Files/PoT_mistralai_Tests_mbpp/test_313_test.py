import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4]), [1, 2, 3, 4])
        self.assertEqual(pos_nos([0, 5, -2, 7]), [0, 5, 7])
        self.assertEqual(pos_nos([-1, -2, -3]), [])
        self.assertEqual(pos_nos([]), [])
        self.assertEqual(pos_nos([-1]), [])

    def test_zero(self):
        self.assertEqual(pos_nos([0]), [0])

    def test_negative_numbers(self):
        self.assertEqual(pos_nos([-1, -2, -3]), [])

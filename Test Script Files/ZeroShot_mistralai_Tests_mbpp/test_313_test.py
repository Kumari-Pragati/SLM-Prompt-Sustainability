import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4, -2, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(pos_nos([]), [])

    def test_single_positive_number(self):
        self.assertEqual(pos_nos([1]), [1])

    def test_single_negative_number(self):
        self.assertEqual(pos_nos([-1]), [])

    def test_single_zero(self):
        self.assertEqual(pos_nos([0]), [])

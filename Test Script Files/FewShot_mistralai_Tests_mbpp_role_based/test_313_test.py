import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(pos_nos([1, 2, 3, -1, 4]), 1)
        self.assertEqual(pos_nos([-1, 0, 1, 2, 3]), 1)
        self.assertEqual(pos_nos([0]), 0)
        self.assertEqual(pos_nos([]), None)
        self.assertEqual(pos_nos([-1, -2, -3]), None)

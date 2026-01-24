import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_pos_nos(self):
        self.assertEqual(pos_nos([-1, -2, -3, 4]), 4)
        self.assertEqual(pos_nos([-1, -2, 0, -3]), 0)
        self.assertEqual(pos_nos([-1, -2, -3, -4]), None)
        self.assertEqual(pos_nos([0, -2, -3, -4]), 0)
        self.assertEqual(pos_nos([1, -2, -3, -4]), 1)

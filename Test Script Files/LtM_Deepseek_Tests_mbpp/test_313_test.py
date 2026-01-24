import unittest
from mbpp_313_code import pos_nos

class TestPosNos(unittest.TestCase):

    def test_pos_nos_simple(self):
        self.assertEqual(pos_nos([-1, 2, 3]), 2)
        self.assertEqual(pos_nos([0, -1, 2]), 0)

    def test_pos_nos_edge(self):
        self.assertEqual(pos_nos([-1, -2]), None)
        self.assertEqual(pos_nos([0]), 0)
        self.assertEqual(pos_nos([]), None)

    def test_pos_nos_complex(self):
        self.assertEqual(pos_nos([-1, -2, 0]), 0)
        self.assertEqual(pos_nos([-1, -2, -3]), None)
        self.assertEqual(pos_nos([-1, -2, -3, 0]), 0)

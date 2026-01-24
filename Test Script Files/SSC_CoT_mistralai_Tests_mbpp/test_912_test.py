import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_lobb_num_typical(self):
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 2), 5)
        self.assertEqual(lobb_num(3, 3), 14)

    def test_lobb_num_edge(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 1)
        self.assertEqual(lobb_num(1, 0), 1)
        self.assertEqual(lobb_num(1, 2), 2)
        self.assertEqual(lobb_num(2, 0), 1)
        self.assertEqual(lobb_num(2, 3), 6)

    def test_lobb_num_boundary(self):
        self.assertEqual(lobb_num(1, 4), 6)
        self.assertEqual(lobb_num(4, 1), 6)
        self.assertEqual(lobb_num(10, 10), 10648)
        self.assertEqual(lobb_num(10, 11), 0)
        self.assertEqual(lobb_num(11, 10), 0)

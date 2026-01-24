import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 2), 5)
        self.assertEqual(lobb_num(3, 3), 14)

    def test_edge_cases(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 1)
        self.assertEqual(lobb_num(1, 0), 1)
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 0), 1)
        self.assertEqual(lobb_num(2, 1), 3)
        self.assertEqual(lobb_num(2, 2), 5)
        self.assertEqual(lobb_num(3, 0), 1)
        self.assertEqual(lobb_num(3, 1), 4)
        self.assertEqual(lobb_num(3, 2), 14)
        self.assertEqual(lobb_num(3, 3), 14)

    def test_boundary_cases(self):
        self.assertEqual(lobb_num(10, 10), 142506)
        self.assertEqual(lobb_num(100, 100), 107150860468795312800)

import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lobb_num(2, 1), 6)
        self.assertEqual(lobb_num(3, 2), 20)
        self.assertEqual(lobb_num(4, 3), 56)

    def test_edge_cases(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(1, 0), 2)
        self.assertEqual(lobb_num(0, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(lobb_num(10, 5), 2520)
        self.assertEqual(lobb_num(20, 10), 184756)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            lobb_num(-1, 2)
        with self.assertRaises(Exception):
            lobb_num(2, -1)
        with self.assertRaises(Exception):
            lobb_num(-1, -1)

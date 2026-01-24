import unittest

from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(lobb_num(3, 2), 6.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(lobb_num(0, 0), 1.0)

    def test_edge_case(self):
        self.assertAlmostEqual(lobb_num(1, 0), 2.0)
        self.assertAlmostEqual(lobb_num(0, 1), 0.0)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            lobb_num(-1, 2)
        with self.assertRaises(Exception):
            lobb_num(2, -1)

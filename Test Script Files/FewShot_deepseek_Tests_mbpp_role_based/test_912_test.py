import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(lobb_num(3, 2), 10.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(lobb_num(0, 0), 1.0)
        self.assertAlmostEqual(lobb_num(1, 0), 2.0)
        self.assertAlmostEqual(lobb_num(0, 1), 1.5)

    def test_edge_conditions(self):
        self.assertAlmostEqual(lobb_num(10, 5), 165.0)
        self.assertAlmostEqual(lobb_num(5, 10), 165.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            lobb_num(-1, 2)
        with self.assertRaises(ValueError):
            lobb_num(2, -1)

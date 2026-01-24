import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_lobb_num_positive(self):
        self.assertEqual(lobb_num(1, 1), 2)
        self.assertEqual(lobb_num(2, 2), 6)
        self.assertEqual(lobb_num(3, 3), 24)
        self.assertEqual(lobb_num(4, 4), 100)

    def test_lobb_num_negative(self):
        self.assertAlmostEqual(lobb_num(-1, 1), 0)
        self.assertAlmostEqual(lobb_num(0, 0), 1)
        self.assertAlmostEqual(lobb_num(1, -1), 0)

    def test_lobb_num_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 0)
        self.assertEqual(lobb_num(1, 0), 0)

    def test_lobb_num_large_inputs(self):
        self.assertAlmostEqual(lobb_num(1000, 1000), 1)
        self.assertAlmostEqual(lobb_num(1000, 1001), 0)
        self.assertAlmostEqual(lobb_num(1001, 1000), 0)

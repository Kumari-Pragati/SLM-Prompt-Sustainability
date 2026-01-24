import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lobb_num(2, 4), 15)
        self.assertEqual(lobb_num(3, 6), 63)
        self.assertEqual(lobb_num(4, 8), 265)

    def test_edge_case_small_n(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 1)
        self.assertEqual(lobb_num(1, 0), 1)

    def test_edge_case_small_m(self):
        self.assertEqual(lobb_num(2, 0), 0)
        self.assertEqual(lobb_num(3, 1), 3)
        self.assertEqual(lobb_num(4, 2), 6)

    def test_edge_case_large_n(self):
        self.assertEqual(lobb_num(10, 20), 120785)
        self.assertEqual(lobb_num(20, 40), 12078495)

    def test_edge_case_large_m(self):
        self.assertEqual(lobb_num(100, 200), 126765060020800)
        self.assertEqual(lobb_num(200, 400), 1267650600208000000000)

    def test_invalid_input_n(self):
        self.assertRaises(TypeError, lobb_num, -1, 2)
        self.assertRaises(TypeError, lobb_num, 1, "m")

    def test_invalid_input_m(self):
        self.assertRaises(TypeError, lobb_num, 2, -1)
        self.assertRaises(TypeError, lobb_num, "n", 2)

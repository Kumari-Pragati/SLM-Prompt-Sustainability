import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lucky_num(5), [2, 4, 6, 8, 10])

    def test_edge_case(self):
        self.assertEqual(lucky_num(1), [2])
        self.assertEqual(lucky_num(0), [])

    def test_boundary_case(self):
        self.assertEqual(lucky_num(10), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lucky_num("5")
        with self.assertRaises(ValueError):
            lucky_num(-5)

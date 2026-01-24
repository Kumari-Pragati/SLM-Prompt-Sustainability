import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(lucky_num(1), [2])
        self.assertEqual(lucky_num(2), [2, 6])
        self.assertEqual(lucky_num(3), [2, 6, 14])

    def test_edge_case(self):
        self.assertEqual(lucky_num(0), [])

    def test_boundary_case(self):
        self.assertEqual(lucky_num(10), [2, 6, 14, 30, 42, 62, 86, 94, 126, 186])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lucky_num("test")
        with self.assertRaises(ValueError):
            lucky_num(-1)

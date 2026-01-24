import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(lucky_num(5), [2, 3, 5, 7, 11])

    def test_boundary_condition(self):
        self.assertEqual(lucky_num(1), [2])

    def test_edge_condition(self):
        self.assertEqual(lucky_num(0), [])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            lucky_num(-1)

import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(22, 7), 21)
        self.assertEqual(round_num(30, 5), 30)

    def test_edge_cases(self):
        self.assertEqual(round_num(0, 1), 0)
        self.assertEqual(round_num(1, 1), 1)
        self.assertEqual(round_num(2, 1), 2)
        self.assertEqual(round_num(4, 2), 4)
        self.assertEqual(round_num(5, 2), 5)
        self.assertEqual(round_num(6, 2), 6)

    def test_boundary_cases(self):
        self.assertEqual(round_num(4, 3), 4)
        self.assertEqual(round_num(5, 3), 5)
        self.assertEqual(round_num(6, 3), 6)
        self.assertEqual(round_num(7, 3), 7)
        self.assertEqual(round_num(8, 3), 8)

import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(lucky_num(1), [2])
        self.assertEqual(lucky_num(2), [2, 6])
        self.assertEqual(lucky_num(3), [2, 6, 14])

    def test_edge_conditions(self):
        self.assertEqual(lucky_num(0), [])
        self.assertEqual(lucky_num(-1), [])

    def test_boundary_conditions(self):
        self.assertEqual(lucky_num(10), [2, 6, 14, 30, 42, 62, 86, 94, 126, 150])

    def test_complex_cases(self):
        self.assertEqual(lucky_num(15), [2, 6, 14, 30, 42, 62, 86, 94, 126, 150, 214, 254, 334, 374, 462])

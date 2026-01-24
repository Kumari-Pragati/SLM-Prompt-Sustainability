import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(20, 5), 20)

    def test_boundary_conditions(self):
        self.assertEqual(round_num(0, 5), 0)
        self.assertEqual(round_num(5, 5), 5)
        self.assertEqual(round_num(10, 1), 10)

    def test_edge_cases(self):
        self.assertEqual(round_num(10, 0), 0)
        self.assertEqual(round_num(0, 10), 0)
        self.assertEqual(round_num(15, 10), 10)
        self.assertEqual(round_num(20, 20), 20)

    def test_complex_cases(self):
        self.assertEqual(round_num(17, 5), 20)
        self.assertEqual(round_num(23, 5), 25)
        self.assertEqual(round_num(30, 10), 30)
        self.assertEqual(round_num(35, 10), 40)

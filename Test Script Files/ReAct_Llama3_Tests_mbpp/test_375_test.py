import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_round_num_typical(self):
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(11, 3), 12)

    def test_round_num_edge_cases(self):
        self.assertEqual(round_num(10.5, 3), 9)
        self.assertEqual(round_num(11.5, 3), 12)

    def test_round_num_boundary_cases(self):
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(11, 1), 11)

    def test_round_num_error_cases(self):
        with self.assertRaises(TypeError):
            round_num('a', 3)

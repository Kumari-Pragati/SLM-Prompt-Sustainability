import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(round_num(15, 5), 15)

    def test_boundary_condition(self):
        self.assertEqual(round_num(0, 5), 0)

    def test_edge_condition(self):
        self.assertEqual(round_num(4, 5), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            round_num('a', 5)

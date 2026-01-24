import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_round_num_typical_use_case(self):
        self.assertEqual(round_num(10, 2), 10)

    def test_round_num_edge_case(self):
        self.assertEqual(round_num(10, 1), 10)

    def test_round_num_boundary_case(self):
        self.assertEqual(round_num(10, 10), 10)

    def test_round_num_negative_number(self):
        self.assertEqual(round_num(-10, 2), -10)

    def test_round_num_zero(self):
        self.assertEqual(round_num(0, 2), 0)

    def test_round_num_invalid_input_type(self):
        with self.assertRaises(TypeError):
            round_num("hello", 2)

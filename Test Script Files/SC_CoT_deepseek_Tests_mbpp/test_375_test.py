import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(round_num(10, 2), 10)
        self.assertEqual(round_num(15, 5), 15)

    def test_boundary_conditions(self):
        self.assertEqual(round_num(0, 1), 0)
        self.assertEqual(round_num(10, 1), 10)

    def test_edge_cases(self):
        self.assertEqual(round_num(3, 2), 4)
        self.assertEqual(round_num(7, 2), 6)

    def test_special_cases(self):
        self.assertEqual(round_num(10, 0), 10)
        self.assertEqual(round_num(0, 10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_num('10', 2)
        with self.assertRaises(TypeError):
            round_num(10, '2')
        with self.assertRaises(ValueError):
            round_num(10, -2)

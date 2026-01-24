import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(22, 7), 21)

    def test_edge_cases(self):
        self.assertEqual(round_num(0, 10), 0)
        self.assertEqual(round_num(10, 0), 10)
        self.assertEqual(round_num(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_num("10", 3)
        with self.assertRaises(TypeError):
            round_num(10, "3")
        with self.assertRaises(TypeError):
            round_num("10", "3")

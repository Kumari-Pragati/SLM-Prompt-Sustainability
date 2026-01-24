import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_round_num_typical(self):
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(12, 3), 12)
        self.assertEqual(round_num(15, 3), 15)
        self.assertEqual(round_num(17, 3), 18)
        self.assertEqual(round_num(20, 3), 18)

    def test_round_num_edge(self):
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(10, 2), 10)
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(10, 4), 8)
        self.assertEqual(round_num(10, 5), 10)

    def test_round_num_invalid(self):
        with self.assertRaises(TypeError):
            round_num('a', 3)
        with self.assertRaises(TypeError):
            round_num(10, 'b')

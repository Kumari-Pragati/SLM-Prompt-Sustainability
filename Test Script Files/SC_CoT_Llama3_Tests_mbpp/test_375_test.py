import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(11, 3), 12)
        self.assertEqual(round_num(12, 3), 12)
        self.assertEqual(round_num(13, 3), 12)
        self.assertEqual(round_num(14, 3), 15)
        self.assertEqual(round_num(15, 3), 15)
        self.assertEqual(round_num(16, 3), 15)
        self.assertEqual(round_num(17, 3), 18)
        self.assertEqual(round_num(18, 3), 18)
        self.assertEqual(round_num(19, 3), 18)
        self.assertEqual(round_num(20, 3), 18)

    def test_edge_cases(self):
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(10, 2), 10)
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(10, 4), 8)
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(10, 6), 10)
        self.assertEqual(round_num(10, 7), 10)
        self.assertEqual(round_num(10, 8), 8)
        self.assertEqual(round_num(10, 9), 10)
        self.assertEqual(round_num(10, 10), 10)

    def test_special_cases(self):
        self.assertEqual(round_num(0, 1), 0)
        self.assertEqual(round_num(0, 2), 0)
        self.assertEqual(round_num(0, 3), 0)
        self.assertEqual(round_num(0, 4), 0)
        self.assertEqual(round_num(0, 5), 0)
        self.assertEqual(round_num(0, 6), 0)
        self.assertEqual(round_num(0, 7), 0)
        self.assertEqual(round_num(0, 8), 0)
        self.assertEqual(round_num(0, 9), 0)
        self.assertEqual(round_num(0, 10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            round_num("a", 3)
        with self.assertRaises(TypeError):
            round_num(10, "a")
        with self.assertRaises(TypeError):
            round_num(None, 3)
        with self.assertRaises(TypeError):
            round_num(10, None)

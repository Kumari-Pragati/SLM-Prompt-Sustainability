import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(round_num(10, 3), 9)
        self.assertEqual(round_num(15, 5), 15)
        self.assertEqual(round_num(22, 7), 21)

    def test_boundary_cases(self):
        self.assertEqual(round_num(0, 1), 0)
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(100, 10), 100)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            round_num("10", 3)
        with self.assertRaises(TypeError):
            round_num(10, "3")
        with self.assertRaises(ValueError):
            round_num(10, 0)

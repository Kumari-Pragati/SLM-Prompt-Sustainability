import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Num(3), 4)

    def test_boundary_case(self):
        self.assertEqual(count_Num(1), 1)

    def test_edge_case(self):
        self.assertEqual(count_Num(2), 2)

    def test_special_case(self):
        self.assertEqual(count_Num(4), 16)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Num('a')

        with self.assertRaises(ValueError):
            count_Num(-1)

        with self.assertRaises(TypeError):
            count_Num(None)

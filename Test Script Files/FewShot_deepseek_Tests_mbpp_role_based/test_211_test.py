import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Num(3), 2)

    def test_boundary_condition(self):
        self.assertEqual(count_Num(1), 1)

    def test_edge_condition(self):
        self.assertEqual(count_Num(0), None)
        self.assertEqual(count_Num(-1), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Num('a')
        with self.assertRaises(TypeError):
            count_Num(2.5)

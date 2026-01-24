import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Num(0), 1)
        self.assertEqual(count_Num(211), 210)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            count_Num('a')
        with self.assertRaises(ValueError):
            count_Num(-1)

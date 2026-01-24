import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Num(3), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)

    def test_edge_cases(self):
        self.assertEqual(count_Num(0), 1)
        self.assertEqual(count_Num(-1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Num('a')
        with self.assertRaises(TypeError):
            count_Num(None)
        with self.assertRaises(TypeError):
            count_Num([])

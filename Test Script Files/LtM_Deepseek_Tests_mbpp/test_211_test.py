import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_Num(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_Num(2), 2)

    def test_complex_cases(self):
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)

import unittest
from mbpp_211_code import count_Num

class TestCountNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Num(0), 0)
        self.assertEqual(count_Num(4), 14)
        self.assertEqual(count_Num(5), 30)
        self.assertEqual(count_Num(6), 62)
        self.assertEqual(count_Num(7), 126)
        self.assertEqual(count_Num(8), 254)
        self.assertEqual(count_Num(9), 508)
        self.assertEqual(count_Num(10), 1010)

    def test_negative_input(self):
        self.assertEqual(count_Num(-1), 0)

    def test_floating_point_input(self):
        self.assertEqual(count_Num(2.5), 16)

    def test_large_positive_input(self):
        self.assertEqual(count_Num(1000), 1048570)

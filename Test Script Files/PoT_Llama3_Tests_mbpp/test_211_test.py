import unittest
from mbpp_211_code import count_Num

class TestCount_Num(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)

    def test_edge_case(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(2), 2)

    def test_boundary_case(self):
        self.assertEqual(count_Num(0), 1)
        self.assertEqual(count_Num(5), 32)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Num('a')

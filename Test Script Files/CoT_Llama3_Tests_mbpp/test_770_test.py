import unittest
from mbpp_770_code import odd_Num_Sum

class Test770Code(unittest.TestCase):

    def test_odd_Num_Sum_typical(self):
        self.assertEqual(odd_Num_Sum(5), 625)

    def test_odd_Num_Sum_edge(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 0)

    def test_odd_Num_Sum_boundary(self):
        self.assertEqual(odd_Num_Sum(3), 81)
        self.assertEqual(odd_Num_Sum(4), 0)

    def test_odd_Num_Sum_invalid(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')

    def test_odd_Num_Sum_negative(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum(-1)

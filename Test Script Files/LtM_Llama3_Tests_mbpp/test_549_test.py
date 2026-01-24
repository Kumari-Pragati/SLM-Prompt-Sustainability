import unittest
from mbpp_549_code import odd_Num_Sum

class TestOdd_Num_Sum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 225)
        self.assertEqual(odd_Num_Sum(3), 1225)
        self.assertEqual(odd_Num_Sum(4), 3375)
        self.assertEqual(odd_Num_Sum(5), 9261)

    def test_edge_cases(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(10), 161051)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')
        with self.assertRaises(TypeError):
            odd_Num_Sum(None)
        with self.assertRaises(TypeError):
            odd_Num_Sum(-1)

import unittest
from mbpp_770_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        self.assertEqual(odd_Num_Sum(2), 17)
        self.assertEqual(odd_Num_Sum(3), 193)
        self.assertEqual(odd_Num_Sum(4), 1297)

    def test_edge_cases(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(-1), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')
        with self.assertRaises(TypeError):
            odd_Num_Sum(None)

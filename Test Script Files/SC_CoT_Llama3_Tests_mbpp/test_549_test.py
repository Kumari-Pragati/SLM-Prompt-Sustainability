import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(odd_Num_Sum(1), 0)
        self.assertEqual(odd_Num_Sum(2), 0)
        self.assertEqual(odd_Num_Sum(3), 225)
        self.assertEqual(odd_Num_Sum(4), 0)
        self.assertEqual(odd_Num_Sum(5), 3375)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(1), 0)
        self.assertEqual(odd_Num_Sum(10), 11025)
        self.assertEqual(odd_Num_Sum(100), 12402500)

    def test_special_and_corner_cases(self):
        self.assertEqual(odd_Num_Sum(-1), 0)
        self.assertEqual(odd_Num_Sum(-10), 0)
        self.assertEqual(odd_Num_Sum(0.5), 0)
        self.assertEqual(odd_Num_Sum(0.1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum("a")
        with self.assertRaises(TypeError):
            odd_Num_Sum([1, 2, 3])
        with self.assertRaises(TypeError):
            odd_Num_Sum({"a": 1})

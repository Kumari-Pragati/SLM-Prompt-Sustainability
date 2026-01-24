import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Sum(10), 20)
        self.assertEqual(Sum(20), 120)
        self.assertEqual(Sum(50), 600)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Sum(0), 0)
        self.assertEqual(Sum(1), 1)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 6)
        self.assertEqual(Sum(5), 6)
        self.assertEqual(Sum(6), 6)
        self.assertEqual(Sum(7), 6)
        self.assertEqual(Sum(8), 12)
        self.assertEqual(Sum(9), 12)
        self.assertEqual(Sum(10), 20)
        self.assertEqual(Sum(100), 164040)
        self.assertEqual(Sum(1000), 142506720)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum(None)
        with self.assertRaises(TypeError):
            Sum("string")
        with self.assertRaises(TypeError):
            Sum([1, 2, 3])

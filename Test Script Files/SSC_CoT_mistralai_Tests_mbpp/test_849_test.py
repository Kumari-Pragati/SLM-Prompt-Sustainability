import unittest
from mbpp_849_code import Sum

class TestSum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Sum(10), 22)
        self.assertEqual(Sum(20), 91)
        self.assertEqual(Sum(30), 167)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Sum(1), 0)
        self.assertEqual(Sum(2), 2)
        self.assertEqual(Sum(3), 3)
        self.assertEqual(Sum(4), 5)
        self.assertEqual(Sum(5), 6)
        self.assertEqual(Sum(6), 6)
        self.assertEqual(Sum(7), 7)
        self.assertEqual(Sum(8), 8)
        self.assertEqual(Sum(9), 12)
        self.assertEqual(Sum(100), 2551)
        self.assertEqual(Sum(1000), 14253)

    def test_special_cases(self):
        self.assertEqual(Sum(12), 22)
        self.assertEqual(Sum(24), 91)
        self.assertEqual(Sum(36), 167)
        self.assertEqual(Sum(48), 266)
        self.assertEqual(Sum(60), 363)
        self.assertEqual(Sum(72), 461)
        self.assertEqual(Sum(84), 558)
        self.assertEqual(Sum(96), 655)
        self.assertEqual(Sum(108), 752)
        self.assertEqual(Sum(120), 850)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Sum, "not_a_number")
        self.assertRaises(TypeError, Sum, -1)
        self.assertRaises(TypeError, Sum, 0)

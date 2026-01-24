import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_Divisors(4), 3)
        self.assertEqual(count_Divisors(6), 4)
        self.assertEqual(count_Divisors(25), 4)
        self.assertEqual(count_Divisors(28), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Divisors(1), 1)
        self.assertEqual(count_Divisors(2), 1)
        self.assertEqual(count_Divisors(3), 2)
        self.assertEqual(count_Divisors(49), 6)
        self.assertEqual(count_Divisors(100), 8)
        self.assertEqual(count_Divisors(221), 8)

    def test_special_cases(self):
        self.assertEqual(count_Divisors(0), "Even")
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(7), "Odd")
        self.assertEqual(count_Divisors(8), "Even")

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Divisors, 'a')
        self.assertRaises(TypeError, count_Divisors, -1)
        self.assertRaises(TypeError, count_Divisors, float('nan'))

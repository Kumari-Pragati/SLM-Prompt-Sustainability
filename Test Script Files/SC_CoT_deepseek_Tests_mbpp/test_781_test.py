import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(4), "Even")
        self.assertEqual(count_Divisors(9), "Odd")
        self.assertEqual(count_Divisors(16), "Even")
        self.assertEqual(count_Divisors(25), "Odd")
        self.assertEqual(count_Divisors(36), "Even")

    def test_edge_cases(self):
        self.assertEqual(count_Divisors(0), "Even")
        self.assertEqual(count_Divisors(1), "Odd")
        self.assertEqual(count_Divisors(2), "Even")
        self.assertEqual(count_Divisors(3), "Odd")

    def test_special_cases(self):
        self.assertEqual(count_Divisors(7), "Odd")
        self.assertEqual(count_Divisors(10), "Even")
        self.assertEqual(count_Divisors(15), "Odd")
        self.assertEqual(count_Divisors(21), "Even")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Divisors("abc")
        with self.assertRaises(TypeError):
            count_Divisors(None)
        with self.assertRaises(TypeError):
            count_Divisors([1,2,3])

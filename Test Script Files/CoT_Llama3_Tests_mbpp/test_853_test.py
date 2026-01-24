import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    def test_sum_of_odd_factors(self):
        self.assertEqual(sum_of_odd_factors(1), 1)
        self.assertEqual(sum_of_odd_factors(2), 3)
        self.assertEqual(sum_of_odd_factors(3), 10)
        self.assertEqual(sum_of_odd_factors(4), 10)
        self.assertEqual(sum_of_odd_factors(5), 20)
        self.assertEqual(sum_of_odd_factors(6), 20)
        self.assertEqual(sum_of_odd_factors(7), 40)
        self.assertEqual(sum_of_odd_factors(8), 40)
        self.assertEqual(sum_of_odd_factors(9), 60)
        self.assertEqual(sum_of_odd_factors(10), 60)
        self.assertEqual(sum_of_odd_factors(11), 90)
        self.assertEqual(sum_of_odd_factors(12), 90)
        self.assertEqual(sum_of_odd_factors(13), 120)
        self.assertEqual(sum_of_odd_factors(14), 120)
        self.assertEqual(sum_of_odd_factors(15), 150)
        self.assertEqual(sum_of_odd_factors(16), 150)
        self.assertEqual(sum_of_odd_factors(17), 180)
        self.assertEqual(sum_of_odd_factors(18), 180)
        self.assertEqual(sum_of_odd_factors(19), 210)
        self.assertEqual(sum_of_odd_factors(20), 210)

    def test_edge_cases(self):
        self.assertEqual(sum_of_odd_factors(0), 1)
        self.assertEqual(sum_of_odd_factors(1), 1)
        self.assertEqual(sum_of_odd_factors(2), 3)
        self.assertEqual(sum_of_odd_factors(3), 10)
        self.assertEqual(sum_of_odd_factors(4), 10)
        self.assertEqual(sum_of_odd_factors(5), 20)
        self.assertEqual(sum_of_odd_factors(6), 20)
        self.assertEqual(sum_of_odd_factors(7), 40)
        self.assertEqual(sum_of_odd_factors(8), 40)
        self.assertEqual(sum_of_odd_factors(9), 60)
        self.assertEqual(sum_of_odd_factors(10), 60)
        self.assertEqual(sum_of_odd_factors(11), 90)
        self.assertEqual(sum_of_odd_factors(12), 90)
        self.assertEqual(sum_of_odd_factors(13), 120)
        self.assertEqual(sum_of_odd_factors(14), 120)
        self.assertEqual(sum_of_odd_factors(15), 150)
        self.assertEqual(sum_of_odd_factors(16), 150)
        self.assertEqual(sum_of_odd_factors(17), 180)
        self.assertEqual(sum_of_odd_factors(18), 180)
        self.assertEqual(sum_of_odd_factors(19), 210)
        self.assertEqual(sum_of_odd_factors(20), 210)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_of_odd_factors("a")
        with self.assertRaises(TypeError):
            sum_of_odd_factors(None)
        with self.assertRaises(TypeError):
            sum_of_odd_factors(1.5)

import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([8, 16]), 16)
        self.assertEqual(get_lcm([15, 30]), 15)

    def test_edge_case_different_primes(self):
        self.assertEqual(get_lcm([2, 3]), 6)
        self.assertEqual(get_lcm([5, 7]), 35)
        self.assertEqual(get_lcm([11, 13]), 11)

    def test_edge_case_same_prime(self):
        self.assertEqual(get_lcm([2, 2]), 4)
        self.assertEqual(get_lcm([5, 5]), 25)
        self.assertEqual(get_lcm([11, 11]), 11)

    def test_edge_case_zero(self):
        self.assertEqual(get_lcm([0, 4]), 0)
        self.assertEqual(get_lcm([4, 0]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(get_lcm([-2, 4]), 4)
        self.assertEqual(get_lcm([4, -2]), 4)

    def test_invalid_input_type(self):
        self.assertRaises(TypeError, get_lcm, [2, "four"])
        self.assertRaises(TypeError, get_lcm, [2, [3, 4]])

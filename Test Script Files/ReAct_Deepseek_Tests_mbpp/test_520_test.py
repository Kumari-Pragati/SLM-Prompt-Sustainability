import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_lcm([2, 7, 3]), 42)

    def test_edge_case_single_number(self):
        self.assertEqual(get_lcm([5]), 5)

    def test_edge_case_two_same_numbers(self):
        self.assertEqual(get_lcm([4, 4]), 4)

    def test_edge_case_two_prime_numbers(self):
        self.assertEqual(get_lcm([3, 7]), 21)

    def test_error_case_empty_list(self):
        with self.assertRaises(IndexError):
            get_lcm([])

    def test_error_case_non_integer_elements(self):
        with self.assertRaises(TypeError):
            get_lcm([2, 'a', 3])

    def test_error_case_negative_numbers(self):
        with self.assertRaises(ValueError):
            get_lcm([2, -1, 3])

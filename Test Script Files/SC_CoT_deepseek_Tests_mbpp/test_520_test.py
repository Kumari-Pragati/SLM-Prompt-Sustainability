import unittest
from mbpp_520_code import get_lcm

class TestGetLCM(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_lcm([2, 7, 3]), 42)

    def test_edge_case_single_number(self):
        self.assertEqual(get_lcm([5]), 5)

    def test_boundary_case_max_limit(self):
        self.assertEqual(get_lcm(list(range(1, 21))), 210)

    def test_special_case_negative_numbers(self):
        self.assertEqual(get_lcm([-2, 7, 3]), 42)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            get_lcm([2, '7', 3])

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            get_lcm([])

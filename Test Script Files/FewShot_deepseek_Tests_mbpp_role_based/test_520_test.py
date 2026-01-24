import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_lcm([2, 7, 3]), 42)

    def test_edge_case_single_number(self):
        self.assertEqual(get_lcm([5]), 5)

    def test_boundary_case_small_numbers(self):
        self.assertEqual(get_lcm([1, 2]), 2)
        self.assertEqual(get_lcm([2, 1]), 2)

    def test_boundary_case_large_numbers(self):
        self.assertEqual(get_lcm([10000, 20000]), 20000)
        self.assertEqual(get_lcm([20000, 10000]), 20000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_lcm("2, 3, 5")
        with self.assertRaises(TypeError):
            get_lcm([2, 3, "5"])
        with self.assertRaises(TypeError):
            get_lcm([2, "3", 5])
        with self.assertRaises(TypeError):
            get_lcm([2, 3, 5, 6, 7, 8, 9, 10])

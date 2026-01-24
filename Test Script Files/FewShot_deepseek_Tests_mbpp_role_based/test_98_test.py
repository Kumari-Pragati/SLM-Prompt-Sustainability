import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 2.4)

    def test_edge_case_single_number(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_boundary_case_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_boundary_case_large_numbers(self):
        self.assertAlmostEqual(multiply_num([10**6, 10**6]), 10**6)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            multiply_num(['1', '2', '3'])

    def test_invalid_input_mixed_types(self):
        with self.assertRaises(TypeError):
            multiply_num([1, '2', 3])

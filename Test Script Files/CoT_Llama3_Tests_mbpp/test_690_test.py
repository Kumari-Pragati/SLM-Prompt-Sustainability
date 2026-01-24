import unittest
from mbpp_690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2, 6, 12])

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_consecutive_nums([]), [])

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(mul_consecutive_nums([1, 1]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums("abc")

    def test_invalid_input_list_with_non_numbers(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums([1, "a", 3, 4, 5])

    def test_invalid_input_list_with_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            mul_consecutive_nums([1.5, 2, 3, 4, 5])

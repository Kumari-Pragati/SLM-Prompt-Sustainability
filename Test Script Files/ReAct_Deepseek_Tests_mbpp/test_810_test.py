import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 'q', 'r', 's'])

    def test_edge_case_with_zero(self):
        self.assertEqual(count_variable(0, 0, 0, 0), ['p', 'q', 'r', 's'])

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(count_variable(-1, -2, -3, -4), ['p', 'q', 'r', 's'])

    def test_edge_case_with_large_numbers(self):
        self.assertEqual(count_variable(1000, 2000, 3000, 4000), ['p', 'q', 'r', 's'])

    def test_error_case_with_non_integer_input(self):
        with self.assertRaises(TypeError):
            count_variable("a", 2, 3, 4)

    def test_error_case_with_too_few_arguments(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2)

    def test_error_case_with_too_many_arguments(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4, 5)

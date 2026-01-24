import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_two(5, 10), 10)

    def test_edge_case_same_values(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_of_two(-5, -10), -5)

    def test_edge_case_one_negative_number(self):
        self.assertEqual(max_of_two(-5, 10), 10)

    def test_error_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            max_of_two(5, 'a')

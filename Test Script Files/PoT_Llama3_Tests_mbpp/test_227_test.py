import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)

    def test_edge_case_a_equal_b(self):
        self.assertEqual(min_of_three(1, 1, 3), 1)

    def test_edge_case_b_equal_c(self):
        self.assertEqual(min_of_three(1, 3, 3), 1)

    def test_edge_case_a_equal_c(self):
        self.assertEqual(min_of_three(3, 1, 3), 1)

    def test_edge_case_a_greater_than_b_and_c(self):
        self.assertEqual(min_of_three(5, 2, 3), 2)

    def test_edge_case_b_greater_than_a_and_c(self):
        self.assertEqual(min_of_three(2, 5, 3), 2)

    def test_edge_case_c_greater_than_a_and_b(self):
        self.assertEqual(min_of_three(2, 3, 5), 2)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_of_three('a', 'b', 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            min_of_three(1, 'b', 3)

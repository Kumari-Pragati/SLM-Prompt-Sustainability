import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1+3+5), (2+4)))

    def test_edge_case_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(sum_of_alternates((1,)), ((1), (0)))

    def test_edge_case_tuple_with_single_element(self):
        self.assertEqual(sum_of_alternates((1, 2)), ((2), (1)))

    def test_edge_case_tuple_with_two_elements(self):
        self.assertEqual(sum_of_alternates((1, 2, 3)), ((1+3), (2)))

    def test_edge_case_tuple_with_three_elements(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4)), ((1+3), (2+4)))

    def test_edge_case_tuple_with_four_elements(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1+3+5), (2+4)))

    def test_edge_case_tuple_with_five_elements(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), ((1+3+5), (2+4+6)))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            sum_of_alternates(123)

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_of_alternates(("a", "b", "c"))

    def test_invalid_input_mixed_type_elements(self):
        with self.assertRaises(TypeError):
            sum_of_alternates((1, "b", 3))

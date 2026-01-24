import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_integer([1]), 1)

    def test_edge_case_single_non_integer_element_list(self):
        self.assertEqual(count_integer(['a']), 0)

    def test_edge_case_multiple_non_integer_elements_list(self):
        self.assertEqual(count_integer(['a', 'b', 'c']), 0)

    def test_edge_case_list_with_multiple_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case_list_with_multiple_integers_and_non_integers(self):
        self.assertEqual(count_integer([1, 2, 3, 'a', 4, 5]), 5)

    def test_edge_case_list_with_negative_integer(self):
        self.assertEqual(count_integer([-1, 2, 3, 4, 5]), 5)

    def test_edge_case_list_with_zero(self):
        self.assertEqual(count_integer([0, 1, 2, 3, 4, 5]), 6)

    def test_edge_case_list_with_mixed_sign_integers(self):
        self.assertEqual(count_integer([-1, 0, 1, 2, 3, 4, 5]), 7)

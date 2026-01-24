import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(find_max([[1]]), 1)

    def test_edge_case_single_element_list_with_negative(self):
        self.assertEqual(find_max([[-1]]), -1)

    def test_edge_case_single_element_list_with_zero(self):
        self.assertEqual(find_max([[0]]), 0)

    def test_edge_case_multiple_negative(self):
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -1)

    def test_edge_case_multiple_positive(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_edge_case_multiple_mixed(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, -6], [7, 8, 9]]), 9)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            find_max("Invalid input")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            find_max(123)

import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(alternate_elements([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(alternate_elements([1]), [])

    def test_edge_case_even_length_list(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_edge_case_odd_length_list(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(alternate_elements([1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(alternate_elements([-1, -2, -3, -4, -5]), [-1, -3, -5])

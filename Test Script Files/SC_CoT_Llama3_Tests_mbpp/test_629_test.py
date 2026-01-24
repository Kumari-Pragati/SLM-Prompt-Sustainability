import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(Split([1]), [])

    def test_edge_case_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_edge_case_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [])

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Split("string")

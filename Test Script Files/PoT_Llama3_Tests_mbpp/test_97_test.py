import unittest
from mbpp_97_code import frequency_lists

class TestFrequencyLists(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(frequency_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]]), {1: 1, 2: 2, 3: 2, 4: 2, 5: 1})

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency_lists([]), {})

    def test_edge_case_single_element_list(self):
        self.assertEqual(frequency_lists([[1]]), {1: 1})

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(frequency_lists([[1, 1, 1]]), {1: 3})

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(frequency_lists([[1, 2, 2, 3, 3, 3]]), {1: 1, 2: 2, 3: 3})

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(frequency_lists([[-1, 0, 1]]), {-1: 1, 0: 1, 1: 1})

    def test_edge_case_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            frequency_lists([['a', 'b', 'c']])

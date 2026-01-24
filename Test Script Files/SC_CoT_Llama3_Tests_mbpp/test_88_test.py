import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_edge_case_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_edge_case_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_edge_case_duplicates(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2]), {1: 2, 2: 3})

    def test_edge_case_duplicates_and_single(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2, 3]), {1: 2, 2: 3, 3: 1})

    def test_edge_case_duplicates_and_single_with_zero(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2, 0, 0]), {1: 2, 2: 3, 0: 2})

    def test_edge_case_duplicates_and_single_with_negative(self):
        self.assertEqual(freq_count([-1, -1, 2, 2, 2, 0, 0]), {-1: 2, 2: 3, 0: 2})

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            freq_count("abc")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            freq_count(123)

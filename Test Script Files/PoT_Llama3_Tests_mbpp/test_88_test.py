import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_edge_case_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_edge_case_single_element_list(self):
        self.assertEqual(freq_count([1]), {1: 1})

    def test_edge_case_duplicates(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2]), {1: 2, 2: 3})

    def test_edge_case_non_integer_values(self):
        self.assertEqual(freq_count([1, 2, 'a', 'a']), {1: 1, 2: 1, 'a': 2})

    def test_edge_case_mixed_types(self):
        self.assertEqual(freq_count([1, 2, 3, 'a', 'b']), {1: 1, 2: 1, 3: 1, 'a': 1, 'b': 1})

import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_element_freq((1, 2, 3, 2, 1)), {1: 2, 2: 2, 3: 1})

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_element_freq(()), {})

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_edge_case_single_element_list(self):
        self.assertEqual(count_element_freq([1]), {1: 1})

    def test_edge_case_empty_list(self):
        self.assertEqual(count_element_freq([]), {})

    def test_edge_case_tuple_of_tuples(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 3), (1, 2))), {1: 2, 2: 2, 3: 1})

    def test_edge_case_tuple_of_lists(self):
        self.assertEqual(count_element_freq([1, 2, 3, 2, 1]), {1: 2, 2: 2, 3: 1})

    def test_edge_case_list_of_tuples(self):
        self.assertEqual(count_element_freq([(1, 2), (2, 3), (1, 2)]), {1: 2, 2: 2, 3: 1})

    def test_edge_case_list_of_lists(self):
        self.assertEqual(count_element_freq([1, 2, 3, 2, 1]), {1: 2, 2: 2, 3: 1})

import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3, 3, 1, 4, 4, 4, 4], 10), 4)

    def test_edge_condition_empty_array(self):
        self.assertEqual(get_odd_occurence([], 0), -1)

    def test_edge_condition_single_element(self):
        self.assertEqual(get_odd_occurence([1], 1), 1)

    def test_edge_condition_all_elements_occur_evenly(self):
        self.assertEqual(get_odd_occurence([1, 2, 1, 2], 4), -1)

    def test_complex_input(self):
        self.assertEqual(get_odd_occurence([1, 2, 2, 3, 3, 1, 4, 4, 4, 4, 5, 5, 5], 13), 5)

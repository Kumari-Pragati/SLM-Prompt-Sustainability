import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
        self.assertEqual(extract_freq(test_list), 3)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(extract_freq(test_list), 0)

    def test_single_sublist(self):
        test_list = [['a', 'b', 'c']]
        self.assertEqual(extract_freq(test_list), 1)

    def test_duplicate_sublists(self):
        test_list = [['a', 'b', 'c'], ['a', 'b', 'c']]
        self.assertEqual(extract_freq(test_list), 1)

    def test_unsorted_sublists(self):
        test_list = [['c', 'b', 'a'], ['b', 'c', 'd']]
        self.assertEqual(extract_freq(test_list), 2)

    def test_empty_sublists(self):
        test_list = [[''], ['']]
        self.assertEqual(extract_freq(test_list), 1)

    def test_single_element_sublists(self):
        test_list = [['a'], ['b'], ['c']]
        self.assertEqual(extract_freq(test_list), 3)

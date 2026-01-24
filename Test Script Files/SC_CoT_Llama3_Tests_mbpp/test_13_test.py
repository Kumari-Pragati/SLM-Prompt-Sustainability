import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_input(self):
        words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
        self.assertEqual(count_common(words), [('banana', 3), ('apple', 2), ('orange', 1)])

    def test_edge_case_empty_list(self):
        words = []
        self.assertEqual(count_common(words), [])

    def test_edge_case_single_word(self):
        words = ['apple']
        self.assertEqual(count_common(words), [('apple', 1)])

    def test_edge_case_single_word_multiple_times(self):
        words = ['apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 3)])

    def test_edge_case_single_word_single_occurrence(self):
        words = ['apple']
        self.assertEqual(count_common(words), [('apple', 1)])

    def test_edge_case_single_word_single_occurrence_multiple_times(self):
        words = ['apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 4)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 5)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge2(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 6)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge3(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 7)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge4(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 8)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge5(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 9)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge6(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 10)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge7(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 11)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge8(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 12)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge9(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 13)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge10(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 14)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge11(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 15)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge12(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple', 'apple']
        self.assertEqual(count_common(words), [('apple', 16)])

    def test_edge_case_single_word_single_occurrence_multiple_times_edge13(self):
        words = ['apple', 'apple', 'apple', 'apple', 'apple
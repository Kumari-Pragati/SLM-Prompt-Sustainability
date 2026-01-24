import unittest
from mbpp_307_code import deepcopy
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_append_to_existing_list(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 10
        expected_result = ([1, 2, 3], [4, 5, 6, 10], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_append_to_nonexistent_list(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 5
        n = 10
        expected_result = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_append_to_empty_tuplex(self):
        tuplex = ()
        m = 0
        n = 10
        expected_result = ([10],)
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_append_to_empty_list(self):
        tuplex = ([], [], [])
        m = 1
        n = 10
        expected_result = ([], [10], [])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

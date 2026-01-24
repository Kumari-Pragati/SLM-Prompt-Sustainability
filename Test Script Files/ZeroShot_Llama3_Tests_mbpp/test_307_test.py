import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_colon_tuplex(self):
        tuplex = [[1, 2, 3], [4, 5, 6]]
        m = 1
        n = 7
        expected_result = [[1, 2, 3], [4, 5, 6], [7]]
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_colon_tuplex_index_out_of_range(self):
        tuplex = [[1, 2, 3], [4, 5, 6]]
        m = 2
        n = 7
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

    def test_colon_tuplex_append_to_empty_list(self):
        tuplex = [[1, 2, 3], [4, 5, 6]]
        m = 0
        n = 7
        expected_result = [[1, 2, 3], [7], [4, 5, 6]]
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

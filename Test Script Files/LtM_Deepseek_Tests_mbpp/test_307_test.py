import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):

    def test_simple_case(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 10
        expected = ([1, 2, 3], [4, 10, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_empty_tuplex(self):
        tuplex = ()
        m = 0
        n = 10
        expected = ()
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_negative_index(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = -1
        n = 10
        expected = ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_out_of_range_index(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 3
        n = 10
        expected = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

    def test_large_number(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 1000000
        expected = ([1, 2, 3], [4, 1000000, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected)

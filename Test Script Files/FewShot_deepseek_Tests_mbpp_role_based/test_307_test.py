import unittest
from mbpp_307_code import colon_tuplex

class TestColonTuplex(unittest.TestCase):
    def test_typical_use_case(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 1
        n = 10
        expected_result = ([1, 2, 3], [4, 10, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_edge_condition(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 0
        n = 10
        expected_result = ([10, 2, 3], [4, 5, 6], [7, 8, 9])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_boundary_condition(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = 2
        n = 10
        expected_result = ([1, 2, 3], [4, 5, 6], [7, 8, 10])
        self.assertEqual(colon_tuplex(tuplex, m, n), expected_result)

    def test_invalid_input(self):
        tuplex = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        m = -1
        n = 10
        with self.assertRaises(IndexError):
            colon_tuplex(tuplex, m, n)

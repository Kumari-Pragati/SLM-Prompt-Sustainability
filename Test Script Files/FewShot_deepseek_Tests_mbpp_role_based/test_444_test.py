import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [('abcde', 'fghij'), ('klmno', 'pqrst')]
        K = 1
        self.assertEqual(trim_tuple(test_list, K), "[(['b', 'd'], ['g', 'i'])]")

    def test_edge_condition(self):
        test_list = [('a', 'b'), ('c', 'd')]
        K = 0
        self.assertEqual(trim_tuple(test_list, K), "[(['a', 'b'], ['c', 'd'])]")

    def test_boundary_condition(self):
        test_list = [('abcdef', 'ghijkl'), ('mnopqr', 'stuvwx')]
        K = 3
        self.assertEqual(trim_tuple(test_list, K), "[(['def'], ['ghi']), (['nopqr'], ['stu'])]")

    def test_invalid_input(self):
        test_list = [('abcde', 'fghij'), ('klmno', 'pqrst')]
        K = 'a'
        with self.assertRaises(TypeError):
            trim_tuple(test_list, K)

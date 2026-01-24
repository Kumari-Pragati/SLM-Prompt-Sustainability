import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('abcde', 'fghij'), ('klmno', 'pqrst')]
        K = 2
        expected_output = "[('cd', 'gh'), ('no', 'rs')]"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_boundary_case(self):
        test_list = [('abcde', 'fghij'), ('klmno', 'pqrst')]
        K = 0
        expected_output = "[('abcde', 'fghij'), ('klmno', 'pqrst')]"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_edge_case(self):
        test_list = [('a', 'b'), ('c', 'd')]
        K = 1
        expected_output = "[('', ''), ('', '')]"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [('abcde', 'fghij'), ('klmno', 'pqrst')]
        K = -1
        with self.assertRaises(IndexError):
            trim_tuple(test_list, K)

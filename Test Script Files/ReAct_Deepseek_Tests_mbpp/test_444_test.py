import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('abcde', 'fghij', 'klmno')]
        K = 2
        expected_output = "(['bcd', 'ghi', 'lmn'])"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_edge_case_K_equals_0(self):
        test_list = [('abcde', 'fghij', 'klmno')]
        K = 0
        expected_output = "(['abcde', 'fghij', 'klmno'])"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_edge_case_K_equals_len_of_string(self):
        test_list = [('abcde', 'fghij', 'klmno')]
        K = 5
        expected_output = "(['', '', ''])"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_error_case_K_greater_than_len_of_string(self):
        test_list = [('abcde', 'fghij', 'klmno')]
        K = 6
        with self.assertRaises(IndexError):
            trim_tuple(test_list, K)

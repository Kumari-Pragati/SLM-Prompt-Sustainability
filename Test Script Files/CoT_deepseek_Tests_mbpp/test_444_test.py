import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('abcde', 'fghij', 'klmno'), ('pqrst', 'uvwxy', 'z')]
        K = 2
        expected_output = "[('cd', 'gh', 'mn'), ('st', 'wx', 'z')]"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_edge_case(self):
        test_list = [('a', 'b', 'c'), ('d', 'e', 'f')]
        K = 1
        expected_output = "[('', ''), ('', '')]"
        self.assertEqual(trim_tuple(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = [('abcde', 'fghij', 'klmno'), ('pqrst', 'uvwxy', 'z')]
        K = 'two'
        with self.assertRaises(TypeError):
            trim_tuple(test_list, K)

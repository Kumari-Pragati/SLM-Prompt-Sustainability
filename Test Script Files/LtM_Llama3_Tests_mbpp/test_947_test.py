import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(len_log([1, 2, 3]), 1)
        self.assertEqual(len_log(['a', 'b', 'c']), 1)
        self.assertEqual(len_log([1, 2, 3, 4]), 1)

    def test_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_single_element(self):
        self.assertEqual(len_log(['hello']), 5)
        self.assertEqual(len_log([123]), 3)

    def test_multiple_elements(self):
        self.assertEqual(len_log(['hello', 'world']), 5)
        self.assertEqual(len_log([123, 456]), 3)

    def test_edge_cases(self):
        self.assertEqual(len_log(['a', 'b', 'c', 'd']), 1)
        self.assertEqual(len_log(['a', 'b', 'c', 'd', 'e']), 1)

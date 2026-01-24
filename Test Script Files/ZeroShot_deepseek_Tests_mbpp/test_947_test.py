import unittest
from mbpp_947_code import len_log

class TestLenLog(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_single_element_list(self):
        self.assertEqual(len_log(['test']), 4)

    def test_multiple_elements_list(self):
        self.assertEqual(len_log(['test', 'testing', 'python']), 4)
        self.assertEqual(len_log(['test', 'short']), 4)
        self.assertEqual(len_log(['longest', 'test', 'short']), 7)

    def test_mixed_type_list(self):
        with self.assertRaises(TypeError):
            len_log(['test', 123, 'python'])

import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_reverse_string_list(self):
        self.assertEqual(reverse_string_list(['abc', 'def', 'ghi']), ['cba', 'fed', 'ihg'])
        self.assertEqual(reverse_string_list(['123', '456', '789']), ['321', '654', '987'])
        self.assertEqual(reverse_string_list(['']), [''], 'Empty string')
        self.assertEqual(reverse_string_list([]), [], 'Empty list')
        self.assertEqual(reverse_string_list(['a']), ['a'], 'Single character')

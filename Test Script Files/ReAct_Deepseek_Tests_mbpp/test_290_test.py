import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_length(['abc', 'defgh', 'ijklmn']), (4, 'defgh'))
        self.assertEqual(max_length(['123', '45678', '9101112']), (6, '45678'))

    def test_edge_cases(self):
        self.assertEqual(max_length(['']), (0, ''))
        self.assertEqual(max_length(['a', 'aa', 'aaa']), (1, 'aaa'))
        self.assertEqual(max_length(['abc', 'defgh', 'ijklmnop']), (8, 'ijklmnop'))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            max_length(123)
        with self.assertRaises(TypeError):
            max_length(['abc', 'defgh', 123])

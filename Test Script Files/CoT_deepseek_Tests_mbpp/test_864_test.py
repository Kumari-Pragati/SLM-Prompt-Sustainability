import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(palindrome_lambda(['radar', 'level', 'python']), ['radar', 'level'])
        self.assertEqual(palindrome_lambda(['madam', 'racecar', 'python']), ['madam', 'racecar'])

    def test_edge_cases(self):
        self.assertEqual(palindrome_lambda(['a']), ['a'])
        self.assertEqual(palindrome_lambda(['']), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            palindrome_lambda(123)
        with self.assertRaises(TypeError):
            palindrome_lambda(['string', 123])
        with self.assertRaises(TypeError):
            palindrome_lambda(['string', None])

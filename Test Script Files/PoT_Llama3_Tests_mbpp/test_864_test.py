import unittest
from mbpp_864_code import palindrome_lambda

class TestPalindromeLambda(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(palindrome_lambda(["radar", "hello", "madam"]), ["radar", "madam"])

    def test_empty_input(self):
        self.assertEqual(palindrome_lambda([]), [])

    def test_single_element_input(self):
        self.assertEqual(palindrome_lambda(["abc"]), [])

    def test_multiple_elements_input(self):
        self.assertEqual(palindrome_lambda(["abc", "def", "cba"]), ["cba"])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            palindrome_lambda([123, "hello", "world"])

    def test_mixed_case_input(self):
        self.assertEqual(palindrome_lambda(["Radar", "Hello", "Madam"]), ["Radar", "Madam"])

    def test_punctuation_input(self):
        self.assertEqual(palindrome_lambda(["A man, a plan, a canal, Panama!"]), ["A man, a plan, a canal, Panama!"])

    def test_spaces_input(self):
        self.assertEqual(palindrome_lambda(["A man, a plan, a canal, Panama! ", "Not a palindrome"]), [])

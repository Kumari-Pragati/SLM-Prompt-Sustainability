import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_length_list([]), (0, ''))

    def test_single_element_list(self):
        self.assertEqual(min_length_list(['hello']), (5, 'hello'))

    def test_multiple_element_list(self):
        self.assertEqual(min_length_list(['hello', 'world', 'python']), (5, 'python'))

    def test_list_with_different_length_strings(self):
        self.assertEqual(min_length_list(['hello', 'world', 'python', 'unittest']), (5, 'python'))

    def test_list_with_same_length_strings(self):
        self.assertEqual(min_length_list(['hello', 'world', 'python', 'unittest', 'test']), (5, 'test'))

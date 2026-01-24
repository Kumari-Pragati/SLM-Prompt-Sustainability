import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        for test_input in ['a', [1], (1,), {1: 1}]:
            self.assertEqual(Find_Max_Length([test_input]), len(str(test_input)))

    def test_multiple_elements_of_same_length(self):
        self.assertEqual(Find_Max_Length(['ab', 'cd', 'ef']), len('abcdef'))

    def test_multiple_elements_of_different_lengths(self):
        self.assertEqual(Find_Max_Length(['ab', 'cd', 'a', 'ef']), len('abcd'))

    def test_negative_list_elements(self):
        self.assertEqual(Find_Max_Length(['-a', '-b', '-c']), len('abc'))

    def test_list_with_empty_strings(self):
        self.assertEqual(Find_Max_Length(['', 'ab', 'cd']), len('abcd'))

    def test_list_with_zero(self):
        self.assertEqual(Find_Max_Length(['a', 0, 'b']), len('ab'))

    def test_list_with_none(self):
        self.assertEqual(Find_Max_Length(['a', None, 'b']), len('ab'))

    def test_list_with_float(self):
        self.assertEqual(Find_Max_Length(['a', 3.14, 'b']), len('ab'))

    def test_list_with_complex(self):
        self.assertEqual(Find_Max_Length(['a', complex(1, 2), 'b']), len('ab'))

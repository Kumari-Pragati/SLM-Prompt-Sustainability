import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element_list(self):
        for element in ['a', [1], (1, 2), 1]:
            self.assertEqual(max_length_list([element]), (len(element), element))

    def test_multiple_elements_same_length(self):
        self.assertEqual(max_length_list(['ab', 'cd', 'ef']), (2, ['ab', 'cd', 'ef']))

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(max_length_list(['ab', 'cd', 'ef', 'ghij']), (4, 'ghij'))

    def test_list_with_tuples_and_strings(self):
        self.assertEqual(max_length_list(['ab', (1, 2), 'cd']), (2, 'cd'))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length_list(['', 'ab', 'cd']), (1, 'ab'))

    def test_list_with_lists_of_different_lengths(self):
        self.assertEqual(max_length_list([[1, 2], [3, 4, 5], [6]]), (3, [3, 4, 5]))

    def test_list_with_negative_lengths(self):
        self.assertEqual(max_length_list([[-1], [-2], [-3]]), (1, [-3]))

    def test_list_with_none(self):
        self.assertEqual(max_length_list([None, 'ab', 'cd']), (3, 'cd'))

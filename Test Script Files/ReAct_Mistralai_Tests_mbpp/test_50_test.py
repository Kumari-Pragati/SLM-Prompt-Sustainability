import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(min_length_list([]))

    def test_single_element_list(self):
        for element in ['a', [1], (1, 2, 3), 1.0]:
            self.assertEqual(min_length_list([element]), (1, element))

    def test_multiple_elements_same_length(self):
        self.assertEqual(min_length_list(['ab', 'cd']), (2, 'ab'))

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(min_length_list(['ab', 'cd', '123']), (3, 'ab'))

    def test_min_length_zero(self):
        self.assertEqual(min_length_list(['', 'abc']), (1, 'abc'))

    def test_min_length_negative(self):
        self.assertEqual(min_length_list(['--', '0', '-1', '2']) , (1, '-1'))

    def test_min_length_none(self):
        self.assertEqual(min_length_list([None, 'abc']), (4, 'abc'))

    def test_min_length_mixed_types(self):
        self.assertEqual(min_length_list(['a', 1, 2.0, [3, 4]]) , (2, 'a'))

import unittest
from mbpp_659_code import Repeat

class TestRepeatFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertListEqual(Repeat(['a']), ['a'])

    def test_duplicate_elements_list(self):
        self.assertListEqual(Repeat(['a', 'a', 'b', 'a']), ['a'])

    def test_no_duplicates_list(self):
        self.assertListEqual(Repeat(['a', 'b', 'c']), [])

    def test_mixed_elements_list(self):
        self.assertListEqual(Repeat(['a', 1, 'a', 'b', 'a']), ['a'])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            Repeat(['a', 'b', 'c'])[0]

    def test_none_type_input(self):
        with self.assertRaises(TypeError):
            Repeat(None)

import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_valid_list_and_string(self):
        self.assertEqual(new_tuple([1, 2, 3], 'four'), ([1, 2, 3, 'four']))

    def test_empty_list_and_string(self):
        self.assertEqual(new_tuple([], 'five'), ([], 'five'))

    def test_list_with_one_element_and_string(self):
        self.assertEqual(new_tuple([6], 'six'), ([6, 'six']))

    def test_list_with_multiple_elements_and_string(self):
        self.assertEqual(new_tuple([7, 8, 9], 'seven'), ([7, 8, 9, 'seven']))

    def test_string_as_list_element(self):
        with self.assertRaises(TypeError):
            new_tuple(['one', 'two'], 'three')

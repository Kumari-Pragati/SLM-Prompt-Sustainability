import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(new_tuple([1, 2, 3], 'test'), (1, 2, 3, 'test'))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], 'empty'), ('empty',))

    def test_single_element_list(self):
        self.assertEqual(new_tuple(['a'], 'single'), ('a', 'single'))

    def test_large_list(self):
        self.assertEqual(new_tuple(list(range(1000)), 'large'), tuple(range(1000)) + ('large',))

    def test_string_in_list(self):
        self.assertEqual(new_tuple(['test', 'string'], 'second'), ('test', 'string', 'second'))

    def test_empty_string(self):
        self.assertEqual(new_tuple([1, 2, 3], ''), (1, 2, 3, ''))

import unittest
from mbpp_709_code import defaultdict
from 709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_unique([]), '{}')

    def test_single_element(self):
        self.assertEqual(get_unique([(1, 'a')]), '{"a": 1}')

    def test_multiple_elements(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'a'), (3, 'b'), (1, 'a'), (2, 'b')]), '{"a": 2, "b": 2}')

    def test_duplicate_values(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'a'), (1, 'b'), (1, 'a')]), '{"a": 3, "b": 1}')

    def test_mixed_values(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'b'), (3, 'a'), (4, 'c'), (1, 'a'), (2, 'b')]), '{"a": 3, "b": 2, "c": 1}')

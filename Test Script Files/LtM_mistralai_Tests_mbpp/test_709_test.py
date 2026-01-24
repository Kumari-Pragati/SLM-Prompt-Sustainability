import unittest
from mbpp_709_code import defaultdict

from709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'a'), (2, 'b'), (1, 'a'), (3, 'c'), (1, 'a'), (2, 'b'), (1, 'a'), (2, 'b'), (1, 'a')]), '{"1": 4, "2": 2, "3": 1}')

    def test_empty_list(self):
        self.assertEqual(get_unique([]), '{}')

    def test_single_item_list(self):
        self.assertEqual(get_unique([(1, 'a')]), '{"1": 1}')

    def test_duplicate_keys(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'b'), (1, 'a'), (1, 'c'), (1, 'a')]), '{"1": 4}')

    def test_different_values_same_key(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b'), (3, 'c')]), '{"1": 3, "2": 2, "3": 3}')

    def test_list_with_none(self):
        self.assertEqual(get_unique([(None, 'a'), (1, 'b'), (1, 'a'), (None, 'c'), (None, 'a')]), '{"1": 2, None: 2}')

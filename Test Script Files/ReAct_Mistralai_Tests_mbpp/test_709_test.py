import unittest
from mbpp_709_code import get_unique

class TestGetUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_unique([]), "{}")

    def test_single_item_list(self):
        self.assertEqual(get_unique([(1, 'a')]), "{'a': 1}")

    def test_multiple_items_same_key(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'a'), (3, 'b'), (4, 'a')]), "{'a': 2, 'b': 1}")

    def test_multiple_items_different_keys(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]), "{'a': 1, 'b': 1, 'c': 1, 'd': 1}")

    def test_list_with_duplicate_tuples(self):
        self.assertEqual(get_unique([(1, 'a'), (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]), "{'a': 2, 'b': 1, 'c': 1, 'd': 1}")

    def test_list_with_none_or_empty_tuple(self):
        self.assertEqual(get_unique([(1, 'a'), (None, 'b'), ((), 'c'), ((),)]), "{'a': 1}")

    def test_list_with_non_tuple_value(self):
        with self.assertRaises(TypeError):
            get_unique([(1, 'a'), (2, 'b'), (3, 'c'), (4, 5)])

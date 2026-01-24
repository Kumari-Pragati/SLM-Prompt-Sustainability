import unittest
from mbpp_709_code import defaultdict
from 709_code import get_unique

class TestGetUnique(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_unique([]), "{}")

    def test_single_element_list(self):
        self.assertEqual(get_unique([(1, 1)]), "{'1': '1'}")

    def test_multiple_elements_same_key(self):
        self.assertEqual(get_unique([(1, 1), (2, 1), (3, 1)]), "{'1': '3'}")

    def test_multiple_elements_different_keys(self):
        self.assertEqual(get_unique([(1, 1), (2, 2), (3, 3)]), "{'1': '1', '2': '1', '3': '1'}")

    def test_mixed_keys_and_values(self):
        self.assertEqual(get_unique([(1, 'a'), (2, 'a'), (3, 'b')]), "{'a': '2', 'b': '1'}")

    def test_duplicate_values(self):
        self.assertEqual(get_unique([(1, 1), (1, 2)]), "{'1': '2'}")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_unique(123)

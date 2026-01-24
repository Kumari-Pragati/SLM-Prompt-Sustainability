import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_remove_empty_list(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_empty_list_with_empty_values(self):
        self.assertEqual(remove_empty([1, 2, None, 4, 5]), [1, 2, 4, 5])

    def test_remove_empty_list_with_empty_strings(self):
        self.assertEqual(remove_empty(["", "hello", "world", "", "test"]), ["hello", "world", "test"])

    def test_remove_empty_list_with_mixed_types(self):
        self.assertEqual(remove_empty([1, "hello", None, 4, "world"]), [1, "hello", 4, "world"])

    def test_remove_empty_list_with_empty_list(self):
        self.assertEqual(remove_empty([[], 1, 2, 3, []]), [1, 2, 3])

    def test_remove_empty_list_with_empty_tuple(self):
        self.assertEqual(remove_empty([(1, 2, 3), 4, 5, (6, 7, 8)],), [1, 2, 3, 4, 5, 6, 7, 8])

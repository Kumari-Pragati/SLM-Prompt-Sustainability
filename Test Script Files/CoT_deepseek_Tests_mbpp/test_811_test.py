import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_different_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_identical_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 2, 3]))

    def test_different_with_duplicates(self):
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2, 3, 2]))

    def test_one_empty_one_non_empty(self):
        self.assertFalse(check_identical([1, 2, 3], []))

    def test_non_list_inputs(self):
        with self.assertRaises(TypeError):
            check_identical("not a list", [1, 2, 3])

        with self.assertRaises(TypeError):
            check_identical([1, 2, 3], "not a list")

        with self.assertRaises(TypeError):
            check_identical("not a list", "not a list")

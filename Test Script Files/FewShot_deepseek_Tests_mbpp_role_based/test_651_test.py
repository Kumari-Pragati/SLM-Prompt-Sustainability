import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))

    def test_empty_tuples(self):
        self.assertTrue(check_subset((), ()))

    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))

    def test_non_subset(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))

    def test_large_tuples(self):
        self.assertTrue(check_subset(tuple(range(1, 10001)), tuple(range(1, 10000))))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_subset((1, 2, 3), "not a tuple")

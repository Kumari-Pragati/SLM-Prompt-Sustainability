import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):
    def test_zip_equal_length_tuples(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(1, 4), (2, 5), (3, 6)])

    def test_zip_shorter_tuple(self):
        self.assertEqual(zip_tuples((1, 2), (3, 4, 5)), [(1, 3), (2, None)])

    def test_zip_longer_tuple(self):
        self.assertEqual(zip_tuples((1, 2), (3, 4, 5, 6)), [(1, 3), (2, 4)])

    def test_zip_empty_tuple(self):
        self.assertEqual(zip_tuples((), (1, 2, 3)), [])

    def test_zip_negative_index(self):
        self.assertEqual(zip_tuples((1, 2), (-1, 0)), [(2, None)])

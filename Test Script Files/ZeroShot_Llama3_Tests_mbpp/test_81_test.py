import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_zip_tuples(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(4, 1), (5, 2), (6, 3)])
        self.assertEqual(zip_tuples((1, 2, 3, 4), (4, 5, 6)), [(4, 1), (5, 2), (6, 3)])
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5), (4, 5, 6)), [(4, 1), (5, 2), (6, 3)])
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5, 6), (4, 5, 6)), [(4, 1), (5, 2), (6, 3)])
        self.assertEqual(zip_tuples((1, 2, 3, 4, 5, 6, 7), (4, 5, 6)), [(4, 1), (5, 2), (6, 3)])

    def test_zip_tuples_empty(self):
        self.assertEqual(zip_tuples((), (4, 5, 6)), [])
        self.assertEqual(zip_tuples((1, 2, 3), ()), [])

    def test_zip_tuples_single(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4,)), [(4, 1)])
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5)), [(4, 1), (5, 2)])

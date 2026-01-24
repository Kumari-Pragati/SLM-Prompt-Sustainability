import unittest
from mbpp_81_code import Tuple
from 81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_zip_tuples(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(1, 4), (2, 5), (3, 6)])
        self.assertEqual(zip_tuples((1, 2, 3, 4), (5, 6)), [(1, 5), (2, 6), (3, None), (4, None)])
        self.assertEqual(zip_tuples((1, 2, 3, 4), (5, 6, 7)), [(1, 5), (2, 6), (3, 7), (4, None)])
        self.assertEqual(zip_tuples((1, 2), (3, 4, 5)), [(1, 3), (2, 4)])
        self.assertEqual(zip_tuples((1, 2, 3), ()), [(1, None), (2, None), (3, None)])
        self.assertEqual(zip_tuples((), (1, 2, 3)), [])

import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_zip_tuples(self):
        self.assertEqual(zip_tuples(('a', 'b', 'c'), (1, 2, 3)), [('a', 1), ('b', 2), ('c', 3)])
        self.assertEqual(zip_tuples(('x', 'y', 'z'), (4, 5)), [('x', 4), ('y', 5), ('z', 4)])
        self.assertEqual(zip_tuples((), ()), [])
        self.assertEqual(zip_tuples(('p', 'q', 'r', 's'), (7, 8, 9)), [('p', 7), ('q', 8), ('r', 9), ('s', 7)])

import unittest
from mbpp_94_code import itemgetter
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_index_minimum(self):
        self.assertEqual(index_minimum([('a', 1), ('b', 2), ('c', 3)]), 'a')
        self.assertEqual(index_minimum([('x', 10), ('y', 2), ('z', 3)]), 'z')
        self.assertEqual(index_minimum([('p', 1), ('q', 2), ('r', 3), ('s', 2)]), 'p')
        self.assertEqual(index_minimum([('m', 10), ('n', 1), ('o', 2), ('p', 3)]), 'n')

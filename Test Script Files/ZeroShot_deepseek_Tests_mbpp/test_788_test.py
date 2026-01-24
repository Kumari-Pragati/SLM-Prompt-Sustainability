import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_new_tuple(self):
        self.assertEqual(new_tuple([1, 2, 3], 'test'), ((1, 2, 3, 'test')))
        self.assertEqual(new_tuple(['a', 'b', 'c'], '123'), (('a', 'b', 'c', '123')))
        self.assertEqual(new_tuple([], 'empty'), (('empty',)))
        self.assertEqual(new_tuple(['one'], 'two'), (('one', 'two')))

import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):

    def test_list_tuple(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))
        self.assertEqual(list_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))
        self.assertEqual(list_tuple([True, False]), (True, False))
        self.assertEqual(list_tuple([1, 'a', True]), (1, 'a', True))
        self.assertEqual(list_tuple([]), ())

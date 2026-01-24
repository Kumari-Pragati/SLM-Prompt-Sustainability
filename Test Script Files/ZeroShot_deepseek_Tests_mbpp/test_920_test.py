import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_remove_tuple(self):
        self.assertEqual(remove_tuple([(None, None), (1, 2), (None, 3), (4, 5)]), '[(1, 2), (None, 3), (4, 5)]')
        self.assertEqual(remove_tuple([(1, 2), (None, None), (3, None), (None, 4)]), '[(1, 2), (3, None), (None, 4)]')
        self.assertEqual(remove_tuple([(None, None), (None, None), (None, None)]), '[]')
        self.assertEqual(remove_tuple([(1, 2), (3, 4), (5, 6)]), '[(1, 2), (3, 4), (5, 6)]')

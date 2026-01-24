import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_remove_matching_tuple(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [2, 3]), [1])
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3], [2]), [1, 3])
        self.assertEqual(remove_matching_tuple([], [1, 2, 3]), [])
        self.assertEqual(remove_matching_tuple([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3], [2, 2]), [1, 3])
        self.assertEqual(remove_matching_tuple([1, 2, 2, 3], [1, 2, 3]), [])

import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTrue(check_none(()))

    def test_single_none(self):
        self.assertTrue(check_none((None,)))

    def test_multiple_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_single_non_none(self):
        self.assertFalse(check_none((1,)))

    def test_mixed_none_non_none(self):
        self.assertTrue(check_none((1, None, 2)))

    def test_list_of_lists(self):
        self.assertTrue(check_none([[None], [None, None], [None, 1]]))

    def test_list_of_tuples(self):
        self.assertTrue(check_none(((None,), (None, None), (None, 1)))

    def test_list_of_sets(self):
        self.assertTrue(check_none({set([None]), set([None, None]), set([None, 1])}))

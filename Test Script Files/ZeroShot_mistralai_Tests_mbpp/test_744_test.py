import unittest
from mbpp_744_code import Tuple

from 744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertTrue(check_none(()))

    def test_tuple_with_none(self):
        self.assertTrue(check_none((None, 1, 2)))

    def test_tuple_with_no_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_tuple_with_mixed_values(self):
        self.assertTrue(check_none((None, 1, None, 2)))

    def test_tuple_with_list_as_element(self):
        self.assertTrue(check_none(([None], 1, 2)))

    def test_tuple_with_set_as_element(self):
        self.assertTrue(check_none(({None}, 1, 2)))

    def test_tuple_with_dict_as_element(self):
        self.assertTrue(check_none(({"None": None}, 1, 2)))

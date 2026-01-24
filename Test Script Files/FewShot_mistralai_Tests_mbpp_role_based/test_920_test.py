import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_tuple([]), "[]")

    def test_single_element_list(self):
        self.assertEqual(remove_tuple([1]), "[1]")

    def test_mixed_list(self):
        self.assertEqual(remove_tuple([1, (1, 2), None, (3, 4), 5]), "[[3, 4], 5]")

    def test_all_tuples(self):
        self.assertEqual(remove_tuple([(1, 2), (3, 4), (5, 6)]), "[]")

    def test_all_none(self):
        self.assertEqual(remove_tuple([None, None, None]), "[]")

    def test_all_empty_tuples(self):
        self.assertEqual(remove_tuple([(), (), ()]], "[]")

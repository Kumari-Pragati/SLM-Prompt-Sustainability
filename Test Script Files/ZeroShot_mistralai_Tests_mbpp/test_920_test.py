import unittest
from mbpp_920_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_tuple([]), "[]")

    def test_single_element(self):
        self.assertEqual(remove_tuple([1]), "[1]")
        self.assertEqual(remove_tuple([None]), "[]")

    def test_multiple_elements(self):
        self.assertEqual(remove_tuple([(1, 2), (3, 4), (None, 5), (6, None)]), "[(1, 2), (3, 4), (6, None)]")

    def test_mixed_list(self):
        self.assertEqual(remove_tuple([1, (1, 2), None, (3, 4), 5, (6, None)]), "[(1, 2), (3, 4), (6, None)]")

import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists(self):
        self.assertEqual(sort_sublists(['dog', 'cat', 'elephant']), ['cat', 'dog', 'elephant'])
        self.assertEqual(sort_sublists(['apple', 'banana', 'cherry']), ['apple', 'banana', 'cherry'])
        self.assertEqual(sort_sublists(['hello', 'world', 'python']), ['hello', 'world', 'python'])
        self.assertEqual(sort_sublists(['a', 'b', 'c']), ['a', 'b', 'c'])
        self.assertEqual(sort_sublists(['short','medium', 'long']), ['short','medium', 'long'])
        self.assertEqual(sort_sublists(['shortest','short','medium', 'longest']), ['shortest','short','medium', 'longest'])

    def test_sort_sublists_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_single_element(self):
        self.assertEqual(sort_sublists(['a']), ['a'])

    def test_sort_sublists_duplicates(self):
        self.assertEqual(sort_sublists(['a', 'b', 'a', 'c']), ['a', 'a', 'b', 'c'])

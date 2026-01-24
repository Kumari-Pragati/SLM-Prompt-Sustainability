import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_new_tuple(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ('1', '2', '3', 'a'))
        self.assertEqual(new_tuple(['a', 'b', 'c'], 'd'), ('a', 'b', 'c', 'd'))
        self.assertEqual(new_tuple([], 'hello'), ('hello'))
        self.assertEqual(new_tuple([1, 2, 3, 4, 5], 'world'), (1, 2, 3, 4, 5, 'world'))
        self.assertEqual(new_tuple(['apple', 'banana', 'cherry'], 'date'), ('apple', 'banana', 'cherry', 'date'))

    def test_new_tuple_empty_list(self):
        self.assertEqual(new_tuple([], 'a'), ('a'))

    def test_new_tuple_empty_string(self):
        self.assertEqual(new_tuple(['a', 'b', 'c'], ''), ('a', 'b', 'c'))

    def test_new_tuple_empty_list_empty_string(self):
        self.assertEqual(new_tuple([], ''), ())

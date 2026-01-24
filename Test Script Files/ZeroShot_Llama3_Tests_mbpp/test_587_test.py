import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):

    def test_list_tuple(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))
        self.assertEqual(list_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))
        self.assertEqual(list_tuple([True, False, True]), (True, False, True))
        self.assertEqual(list_tuple([1.0, 2.0, 3.0]), (1.0, 2.0, 3.0))
        self.assertEqual(list_tuple([1, 2, 3, 4, 5]), (1, 2, 3, 4, 5))
        self.assertEqual(list_tuple([]), ())
        self.assertEqual(list_tuple([1]), (1,))
        self.assertEqual(list_tuple([1, 2]), (1, 2))

    def test_list_tuple_empty(self):
        self.assertEqual(list_tuple([]), ())

    def test_list_tuple_single_element(self):
        self.assertEqual(list_tuple([1]), (1,))

    def test_list_tuple_multiple_elements(self):
        self.assertEqual(list_tuple([1, 2, 3, 4, 5]), (1, 2, 3, 4, 5))

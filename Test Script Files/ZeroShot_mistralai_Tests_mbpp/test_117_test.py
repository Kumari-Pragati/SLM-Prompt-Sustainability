import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(list_to_float([]), "[]")

    def test_single_element_list(self):
        self.assertEqual(list_to_float([['a', 1.0]]), "[('a', 1.0)]")

    def test_mixed_list(self):
        self.assertEqual(list_to_float([['a', 1.0], ['b', 2.0], ['c', 3.0]]), "[('a', 1.0), ('b', 2.0), ('c', 3.0)]")

    def test_list_with_only_strings(self):
        self.assertEqual(list_to_float([['a', 'b', 'c']]), "[('a',), ('b',), ('c',)]")

    def test_list_with_only_floats(self):
        self.assertEqual(list_to_float([[1.0, 2.0, 3.0]]), "[(None, 1.0), (None, 2.0), (None, 3.0)]")

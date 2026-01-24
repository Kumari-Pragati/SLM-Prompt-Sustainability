import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element(self):
        self.assertEqual(Extract([('a',)]), ['a'])

    def test_duplicate_elements(self):
        self.assertEqual(Extract([('a', 1), ('a', 2)]), ['a', 'a'])

    def test_large_list(self):
        self.assertEqual(Extract([(i, i+1) for i in range(100)]), list(range(100)))

    def test_non_string_elements(self):
        self.assertEqual(Extract([(1, 2), (3, 4)]), [1, 3])

    def test_none_elements(self):
        self.assertEqual(Extract([(None, 1), (None, 2)]), [None, None])

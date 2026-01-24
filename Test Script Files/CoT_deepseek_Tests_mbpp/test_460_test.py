import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item(self):
        self.assertEqual(Extract([('a', 1)]), ['a'])

    def test_duplicate_items(self):
        self.assertEqual(Extract([('a', 1), ('a', 2)]), ['a', 'a'])

    def test_non_tuple_items(self):
        with self.assertRaises(TypeError):
            Extract([1, 2, 3])

    def test_non_string_first_element(self):
        with self.assertRaises(TypeError):
            Extract([(1, 2), (3, 4)])

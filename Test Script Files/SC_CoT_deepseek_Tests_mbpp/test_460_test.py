import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item_list(self):
        self.assertEqual(Extract([('a',)]), ['a'])

    def test_list_with_none_values(self):
        self.assertEqual(Extract([(None, 1), (None, 2)]), [None, None])

    def test_list_with_mixed_types(self):
        self.assertEqual(Extract([(1, 'a'), (2, 'b')]), [1, 2])

    def test_list_with_non_tuple_items(self):
        with self.assertRaises(TypeError):
            Extract(['a', 'b'])

    def test_list_with_empty_tuples(self):
        with self.assertRaises(ValueError):
            Extract([(), ()])

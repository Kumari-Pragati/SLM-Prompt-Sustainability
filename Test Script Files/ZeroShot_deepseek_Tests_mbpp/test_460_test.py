import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_single_item(self):
        self.assertEqual(Extract([('a', 1)]), ['a'])

    def test_multiple_items(self):
        self.assertEqual(Extract([('a', 1), ('b', 2)]), ['a', 'b'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            Extract([('a', 1), 2])

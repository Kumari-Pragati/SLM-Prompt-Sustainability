import unittest
from mbpp_460_code import Extract

class TestExtractFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Extract([(1,), (2, 3), (4, 5, 6)]), [1, 2, 4])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_item(self):
        self.assertEqual(Extract([(5,)]), [5])

    def test_list_of_tuples_with_single_item(self):
        self.assertEqual(Extract([(1,), (2,), (3,)]), [1, 2, 3])

    def test_list_of_tuples_with_multiple_items(self):
        self.assertEqual(Extract([(1, 2), (3, 4), (5, 6, 7)]), [1, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(Extract([(-1,), (-2,), (-3,)]), [-1, -2, -3])

    def test_floats(self):
        self.assertEqual(Extract([(1.1,), (2.2,), (3.3,)]), [1.1, 2.2, 3.3])

    def test_strings(self):
        self.assertEqual(Extract([('a',), ('b',), ('c',)]), ['a', 'b', 'c'])

    def test_empty_tuple(self):
        self.assertEqual(Extract([(), (), ((),)]), [])

import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c', 'd']), 3)

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), ['a', 'b', 'c', 'd']), 0)

    def test_empty_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), []), 0)

    def test_all_items_in_tuple(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c']), 3)

    def test_no_items_in_tuple(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e', 'f']), 0)

    def test_duplicate_items_in_tuple(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'b'), ['a', 'b', 'c']), 3)

    def test_duplicate_items_in_list(self):
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'a', 'b']), 3)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            count_Occurrence(123, ['a', 'b', 'c'])

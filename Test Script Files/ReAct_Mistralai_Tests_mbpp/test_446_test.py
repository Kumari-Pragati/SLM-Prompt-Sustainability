import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_Occurrence((), []), 0)

    def test_single_element_tuple(self):
        self.assertEqual(count_Occurrence((1,), [1]), 1)
        self.assertEqual(count_Occurrence((1.0), [1]), 1)
        self.assertEqual(count_Occurrence(('a',), ['a']), 1)

    def test_multiple_elements_tuple(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [1, 2, 3, 4]), 3)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['a', 'b', 'c', 'd']), 3)

    def test_non_matching_elements(self):
        self.assertEqual(count_Occurrence((1, 2, 3), [4, 5, 6]), 0)
        self.assertEqual(count_Occurrence(('a', 'b', 'c'), ['d', 'e', 'f']), 0)

    def test_none_type_elements(self):
        self.assertRaises(TypeError, lambda: count_Occurrence((None,), [None]))
        self.assertRaises(TypeError, lambda: count_Occurrence((1,), [None]))
        self.assertRaises(TypeError, lambda: count_Occurrence([None], (1, 2, 3)))

    def test_mixed_types(self):
        self.assertEqual(count_Occurrence(('a', 1), ['a', 1]), 2)
        self.assertEqual(count_Occurrence((1.0, 'b'), [1.0, 'b']), 2)

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), ['a']), 0)
        self.assertEqual(count_Occurrence([], (1, 2, 3)), 0)

    def test_single_element_list(self):
        self.assertEqual(count_Occurrence([1], (1, 2, 3)), 1)
        self.assertEqual(count_Occurrence(['a'], ('a', 'b', 'c')), 1)

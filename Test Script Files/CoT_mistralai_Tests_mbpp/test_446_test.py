import unittest
from mbpp_446_code import count_Occurrence

class TestCountOccurrence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_Occurrence((), []), 0)

    def test_empty_tuple(self):
        self.assertEqual(count_Occurrence((), (1, 2, 3)), 0)

    def test_single_element_tuple(self):
        self.assertEqual(count_Occurrence((1), [1, 2, 3]), 1)

    def test_single_element_list(self):
        self.assertEqual(count_Occurrence((1), [1]), 1)

    def test_multiple_elements_tuple(self):
        self.assertEqual(count_Occurrence((1, 2), [1, 2, 3]), 1)
        self.assertEqual(count_Occurrence((1, 2), [2, 1, 3]), 2)

    def test_multiple_elements_list(self):
        self.assertEqual(count_Occurrence((1, 2), [2, 1, 3]), 2)
        self.assertEqual(count_Occurrence((1, 2), [3, 1, 2]), 1)

    def test_non_matching_elements(self):
        self.assertEqual(count_Occurrence((1, 2), [3, 4, 5]), 0)

    def test_none_type_input(self):
        self.assertRaises(TypeError, count_Occurrence, (1, 2), None)

    def test_string_input(self):
        self.assertRaises(TypeError, count_Occurrence, (1, 2), "abc")

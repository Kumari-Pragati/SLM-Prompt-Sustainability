import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(most_common_elem('a', 1), [('a', 1)])

    def test_multiple_elements(self):
        self.assertEqual(most_common_elem('aaabbc', 2), [('a', 3), ('b', 2)])

    def test_empty_string(self):
        self.assertEqual(most_common_elem('', 1), [])

    def test_single_character_list(self):
        self.assertEqual(most_common_elem(['a'], 1), [('a', 1)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            most_common_elem(123, 1)

    def test_negative_number_of_elements(self):
        with self.assertRaises(ValueError):
            most_common_elem('abc', -1)

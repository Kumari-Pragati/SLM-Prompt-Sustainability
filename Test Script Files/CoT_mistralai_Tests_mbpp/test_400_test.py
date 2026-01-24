import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element_list(self):
        self.assertEqual(extract_freq([(1, 2)]), 1)

    def test_multiple_elements_same_frequency(self):
        self.assertEqual(extract_freq([(1, 2), (2, 1)]), 1)

    def test_multiple_elements_different_frequency(self):
        self.assertEqual(extract_freq([(1, 2), (2, 3), (3, 2)]), 2)

    def test_duplicate_sublists(self):
        self.assertEqual(extract_freq([[(1, 2), (2, 1)], [(1, 2), (2, 1)]]), 1)

    def test_sorted_sublists(self):
        self.assertEqual(extract_freq([[(2, 1), (1, 2)], [(1, 2), (2, 1)]]), 1)

    def test_negative_numbers(self):
        self.assertEqual(extract_freq([((-1, 2), (1, 3)), ((1, 2), (-1, 3))]), 1)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            extract_freq([(1, 2), (2, 'a')])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_freq('invalid input')

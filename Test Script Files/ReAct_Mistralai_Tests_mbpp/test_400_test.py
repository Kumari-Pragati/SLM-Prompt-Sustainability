import unittest
from mbpp_400_code import extract_freq

class TestExtractFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(extract_freq([]), 0)

    def test_single_element_list(self):
        self.assertEqual(extract_freq([(1, 2)]), 1)

    def test_duplicate_elements_list(self):
        self.assertEqual(extract_freq([(1, 2), (1, 2)]), 1)

    def test_multiple_unique_elements_list(self):
        self.assertEqual(extract_freq([(1, 2), (2, 3), (3, 4)]), 3)

    def test_mixed_elements_list(self):
        self.assertEqual(extract_freq([(1, 2), (2, 3), (3, 4), (2, 1)]), 2)

    def test_sorted_list_with_same_elements(self):
        self.assertEqual(extract_freq([(2, 1), (1, 2)]), 1)

    def test_list_with_only_tuples(self):
        self.assertEqual(extract_freq([(1, 2), (1, 2.0), (1, 2, 3)]), 1)

    def test_list_with_non_tuples(self):
        with self.assertRaises(TypeError):
            extract_freq([1, 2, 3])

    def test_list_with_empty_tuples(self):
        self.assertEqual(extract_freq([(), (), (1,)]), 1)

    def test_list_with_single_empty_tuple(self):
        self.assertEqual(extract_freq([(1,), ()]), 1)

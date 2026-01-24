import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_elements([1, 2, 3, 1, 2, 3, 1], 2), [(1, 2), (3, 1)])

    def test_edge_case_single_element(self):
        self.assertEqual(extract_elements([1], 1), [(1,)])

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_elements([], 1), [])

    def test_edge_case_single_group(self):
        self.assertEqual(extract_elements([1, 1], 1), [(1, 1)])

    def test_edge_case_multiple_groups(self):
        self.assertEqual(extract_elements([1, 2, 1, 2], 1), [(1,), (2,)])

    def test_edge_case_longer_group(self):
        self.assertEqual(extract_elements([1, 1, 2], 2), [(1, 1)])

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            extract_elements([1, 2, 3], 0)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            extract_elements("123", 1)

import unittest
from mbpp_140_code import extract_singly

class TestExtractSingly(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_edge_condition(self):
        test_list = []
        expected_output = []
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_boundary_condition(self):
        test_list = [[1]]
        expected_output = [1]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected_output = [1, 2, 3]
        self.assertEqual(extract_singly(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [1, 2, 3]
        with self.assertRaises(TypeError):
            extract_singly(test_list)

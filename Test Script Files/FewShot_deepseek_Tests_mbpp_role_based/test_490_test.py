import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2), (2, 1), (3, 4), (4, 3)]
        expected_output = {(1, 2), (3, 4)}
        self.assertEqual(extract_symmetric(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = set()
        self.assertEqual(extract_symmetric(test_list), expected_output)

    def test_single_element(self):
        test_list = [(1, 1)]
        expected_output = set()
        self.assertEqual(extract_symmetric(test_list), expected_output)

    def test_duplicate_elements(self):
        test_list = [(1, 2), (2, 1), (1, 2)]
        expected_output = {(1, 2), (2, 1)}
        self.assertEqual(extract_symmetric(test_list), expected_output)

    def test_same_elements(self):
        test_list = [(1, 1), (2, 2)]
        expected_output = set()
        self.assertEqual(extract_symmetric(test_list), expected_output)

    def test_invalid_input(self):
        test_list = [(1, 2), 'a', (3, 4)]
        with self.assertRaises(TypeError):
            extract_symmetric(test_list)

import unittest
from mbpp_13_code import count_common

class TestCountCommon(unittest.TestCase):
    def test_typical_use_case(self):
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']
        expected_output = [('cherry', 3), ('banana', 2), ('apple', 2)]
        self.assertEqual(count_common(words), expected_output)

    def test_edge_case_single_word(self):
        words = ['apple']
        expected_output = [('apple', 1)]
        self.assertEqual(count_common(words), expected_output)

    def test_boundary_case_empty_list(self):
        words = []
        expected_output = []
        self.assertEqual(count_common(words), expected_output)

    def test_boundary_case_single_unique_word(self):
        words = ['apple', 'banana', 'cherry']
        expected_output = [('apple', 1), ('banana', 1), ('cherry', 1)]
        self.assertEqual(count_common(words), expected_output)

    def test_error_handling(self):
        words = ['apple', 123, 'cherry']
        with self.assertRaises(TypeError):
            count_common(words)

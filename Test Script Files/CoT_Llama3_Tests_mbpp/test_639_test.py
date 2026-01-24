import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sample_nam(['HelloWorld', 'Hello123', 'helloWorld']), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(sample_nam(['HelloWorld']), 1)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(sample_nam(['HelloWorld', 'helloWorld', 'HELLO123']), 2)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sample_nam('Invalid Input')

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            sample_nam([1, 2, 3])

    def test_invalid_input_non_string_element(self):
        with self.assertRaises(TypeError):
            sample_nam(['Hello', 123, 'World'])

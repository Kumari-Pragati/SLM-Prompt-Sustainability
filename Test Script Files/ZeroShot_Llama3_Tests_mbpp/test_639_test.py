import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_single_element(self):
        self.assertEqual(sample_nam(['HelloWorld']), 10)

    def test_multiple_elements(self):
        self.assertEqual(sample_nam(['HelloWorld', 'GoodbyeWorld', 'PythonIsFun']), 24)

    def test_mixed_case(self):
        self.assertEqual(sample_nam(['hello', 'WORLD', 'PythonIsFun']), 17)

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            sample_nam([1, 2, 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sample_nam('HelloWorld')

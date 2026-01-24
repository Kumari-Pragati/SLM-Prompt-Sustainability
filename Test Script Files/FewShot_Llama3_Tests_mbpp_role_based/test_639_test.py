import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_use_case(self):
        sample_names = ["HelloWorld", "GoodbyeWorld", "PythonIsFun"]
        self.assertEqual(sample_nam(sample_names), 3)

    def test_empty_list(self):
        sample_names = []
        self.assertEqual(sample_nam(sample_names), 0)

    def test_single_element_list(self):
        sample_names = ["HelloWorld"]
        self.assertEqual(sample_nam(sample_names), 1)

    def test_multiple_elements_list(self):
        sample_names = ["HelloWorld", "GoodbyeWorld", "PythonIsFun", "JavaIsCool"]
        self.assertEqual(sample_nam(sample_nam(sample_names)), 3)

    def test_non_string_elements(self):
        sample_names = ["HelloWorld", 123, "GoodbyeWorld", "PythonIsFun"]
        with self.assertRaises(TypeError):
            sample_nam(sample_names)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            sample_nam("HelloWorld")

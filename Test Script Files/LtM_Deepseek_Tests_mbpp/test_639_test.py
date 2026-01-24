import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(sample_nam(['Apple', 'Banana', 'Cherry']), 10)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_boundary_case_single_uppercase(self):
        self.assertEqual(sample_nam(['Apple']), 5)

    def test_boundary_case_single_lowercase(self):
        self.assertEqual(sample_nam(['apple']), 0)

    def test_complex_case_mixed_case(self):
        self.assertEqual(sample_nam(['ApPle', 'BaNaNa', 'ChErRy']), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sample_nam(123)

    def test_invalid_input_mixed_types(self):
        with self.assertRaises(TypeError):
            sample_nam(['Apple', 123, 'Cherry'])

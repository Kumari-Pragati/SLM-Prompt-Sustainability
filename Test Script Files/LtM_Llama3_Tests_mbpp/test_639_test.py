import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sample_nam([]), 0)

    def test_single_input(self):
        self.assertEqual(sample_nam(['HelloWorld']), 1)

    def test_multiple_inputs(self):
        self.assertEqual(sample_nam(['HelloWorld', 'GoodBye']), 2)

    def test_edge_case_input(self):
        self.assertEqual(sample_nam(['HelloWorld', 'goodbye']), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sample_nam([123, 'HelloWorld'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sample_nam({'HelloWorld'})

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            sample_nam(['HelloWorld', 123])

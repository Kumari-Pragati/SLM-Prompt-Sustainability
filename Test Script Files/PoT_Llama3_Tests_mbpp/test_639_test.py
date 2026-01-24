import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sample_nam(['HelloWorld', 'HelloWorld1', 'HelloWorld2']), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(sample_nam(['HelloWorld']), 1)

    def test_edge_case_all_uppercase(self):
        self.assertEqual(sample_nam(['HELLO', 'HELLO1', 'HELLO2']), 3)

    def test_edge_case_all_lowercase(self):
        self.assertEqual(sample_nam(['hello', 'hello1', 'hello2']), 0)

    def test_edge_case_mixed_case(self):
        self.assertEqual(sample_nam(['Hello', 'hello', 'Hello1']), 1)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            sample_nam([123, 'Hello', 'hello'])

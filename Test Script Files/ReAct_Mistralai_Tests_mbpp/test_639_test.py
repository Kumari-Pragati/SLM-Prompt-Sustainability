import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_single_name(self):
        self.assertEqual(sample_nam(['Abbott', 'Costello']), 1)

    def test_multiple_names(self):
        self.assertEqual(sample_nam(['Alice', 'Bob', 'Charlie']), 3)

    def test_mixed_case_names(self):
        self.assertEqual(sample_nam(['AlIcE', 'bOb', 'ChArLiE']), 3)

    def test_no_uppercase_names(self):
        self.assertEqual(sample_nam(['alice', 'bob', 'charlie']), 0)

    def test_all_uppercase_names(self):
        self.assertEqual(sample_nam(['AA', 'BB', 'CC']), 3)

    def test_all_lowercase_names(self):
        self.assertEqual(sample_nam(['a', 'b', 'c']), 0)

    def test_single_digit_names(self):
        self.assertEqual(sample_nam(['1', '2', '3']), 0)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sample_nam([1, 'A'])

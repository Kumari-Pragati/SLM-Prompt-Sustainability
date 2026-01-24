import unittest
from mbpp_13_code import Counter
from 13_code import count_common

class TestCountCommon(unittest.TestCase):

    def test_typical_case(self):
        words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']
        expected_output = [('cherry', 3), ('banana', 2), ('apple', 2)]
        self.assertEqual(count_common(words), expected_output)

    def test_edge_case(self):
        words = []
        expected_output = []
        self.assertEqual(count_common(words), expected_output)

    def test_boundary_case(self):
        words = ['apple'] * 10000
        expected_output = [('apple', 10000)]
        self.assertEqual(count_common(words), expected_output)

    def test_special_case(self):
        words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'apple', 'banana', 'cherry', 'date', 'fig', 'grape']
        expected_output = [('grape', 2), ('date', 2), ('cherry', 2), ('banana', 2), ('apple', 2)]
        self.assertEqual(count_common(words), expected_output)

    def test_invalid_input(self):
        words = [1, 2, 3, 4]
        with self.assertRaises(TypeError):
            count_common(words)

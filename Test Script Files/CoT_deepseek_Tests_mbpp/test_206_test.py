import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c', 'd')), ('ab', 'bc', 'cd'))

    def test_single_element(self):
        self.assertEqual(concatenate_elements(('a',)), ())

    def test_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_large_tuple(self):
        self.assertEqual(concatenate_elements(('a',) * 1000), tuple(''.join(i + j for i, j in zip(('a',) * 1000, ('a',) * 999))) + ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements(123)
        with self.assertRaises(TypeError):
            concatenate_elements(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            concatenate_elements(('a', 1))

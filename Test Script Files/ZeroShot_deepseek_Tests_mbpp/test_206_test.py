import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(concatenate_elements(('a',)), ('a',))

    def test_two_elements(self):
        self.assertEqual(concatenate_elements(('a', 'b')), ('ab',))

    def test_multiple_elements(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c')), ('ab', 'bc'))

    def test_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_large_tuple(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c', 'd', 'e')), ('ab', 'bc', 'cd'))

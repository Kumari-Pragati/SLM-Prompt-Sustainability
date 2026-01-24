import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c', 'd')), ('ab', 'bc', 'cd'))

    def test_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_elements(('x',)), ())

    def test_two_elements_tuple(self):
        self.assertEqual(concatenate_elements(('1', '2')), ('12',))

    def test_large_tuple(self):
        self.assertEqual(concatenate_elements(('1', '2', '3', '4', '5')), ('12', '23', '34', '45'))

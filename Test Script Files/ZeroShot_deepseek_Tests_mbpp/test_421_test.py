import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_multiple_elements_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_string_elements_tuple(self):
        self.assertEqual(concatenate_tuple(('a', 'b', 'c')), 'a-b-c')

    def test_mixed_elements_tuple(self):
        self.assertEqual(concatenate_tuple((1, 'a', 2.5)), '1-a-2.5')

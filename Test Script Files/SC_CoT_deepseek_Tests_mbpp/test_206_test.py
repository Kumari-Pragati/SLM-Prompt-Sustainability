import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c', 'd')), 
                         (('ab', 'bc', 'cd'),))

    def test_single_element(self):
        self.assertEqual(concatenate_elements(('a',)), 
                         ((),))

    def test_empty_tuple(self):
        self.assertEqual(concatenate_elements(()), 
                         ((),))

    def test_large_tuple(self):
        self.assertEqual(concatenate_elements(('a',) * 1000), 
                         (('a' * 999,),))

    def test_numeric_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), 
                         ((12, 23),))

    def test_special_characters(self):
        self.assertEqual(concatenate_elements(('!', '@', '#', '$')), 
                         (('!@', '@#'),))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            concatenate_elements(12345)

        with self.assertRaises(TypeError):
            concatenate_elements(('a', 'b', 'c', 'd', 'e', 'f'))

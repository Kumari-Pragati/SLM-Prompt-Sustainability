import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c')), ('ab', 'bc'))

    def test_edge_conditions(self):
        self.assertEqual(concatenate_elements(('')), ())
        self.assertEqual(concatenate_elements(('a')), ())

    def test_complex_cases(self):
        self.assertEqual(concatenate_elements(('1', '2', '3', '4')), ('12', '23', '34'))
        self.assertEqual(concatenate_elements(('hello', 'world')), ('helloworld'))

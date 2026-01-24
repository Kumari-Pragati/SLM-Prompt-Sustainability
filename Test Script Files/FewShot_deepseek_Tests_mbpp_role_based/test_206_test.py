import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_elements(('a', 'b', 'c')), (('ab', 'bc'),))

    def test_edge_condition(self):
        self.assertEqual(concatenate_elements(('a',)), ((),))

    def test_boundary_condition(self):
        self.assertEqual(concatenate_elements(()), ((),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_elements(123)

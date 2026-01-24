import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), ((2, 6), (6, 12)))

    def test_edge_case(self):
        self.assertEqual(multiply_elements((1,)), ())

    def test_boundary_case(self):
        self.assertEqual(multiply_elements((1, 2)), ((2,),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply_elements(123)
        with self.assertRaises(TypeError):
            multiply_elements((1, 2, 'a'))

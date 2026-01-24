import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (2, 3, 4))
        self.assertEqual(concatenate_elements((5, 6, 7, 8)), (6, 7, 8))

    def test_edge_cases(self):
        self.assertEqual(concatenate_elements((1, 2)), (2,))
        self.assertEqual(concatenate_elements((1, 2, 3)), (2, 3))
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (2, 3, 4, 5))

    def test_empty_input(self):
        self.assertRaises(TypeError, concatenate_elements, ())

    def test_single_element_input(self):
        self.assertRaises(TypeError, concatenate_elements, (1,))

    def test_non_tuple_input(self):
        self.assertRaises(TypeError, concatenate_elements, [1, 2, 3])

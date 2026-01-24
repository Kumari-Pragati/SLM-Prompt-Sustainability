import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (1, 3, 5))
        self.assertEqual(concatenate_elements((4, 5, 6)), (4, 6, 10))

    def test_edge_cases(self):
        self.assertEqual(concatenate_elements((1,)), (1,))
        self.assertEqual(concatenate_elements((1, 2)), (1, 2, 2))
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (1, 3, 5, 6))

    def test_complex_cases(self):
        self.assertEqual(concatenate_elements((-1, 0, 1)), (-1, 0, 1))
        self.assertEqual(concatenate_elements((10, 20, 30)), (10, 30, 50))
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (1, 3, 5, 7, 9))

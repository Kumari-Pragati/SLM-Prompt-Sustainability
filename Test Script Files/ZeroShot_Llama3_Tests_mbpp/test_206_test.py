import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_concatenate_elements(self):
        self.assertEqual(concatenate_elements((1, 2, 3)), (3, 4, 5))
        self.assertEqual(concatenate_elements((1, 2, 3, 4)), (3, 4, 5, 6))
        self.assertEqual(concatenate_elements((1, 2, 3, 4, 5)), (3, 4, 5, 6, 7))
        self.assertEqual(concatenate_elements((1, 2)), (3,))
        self.assertEqual(concatenate_elements((1)), ())

    def test_concatenate_elements_edge_cases(self):
        self.assertEqual(concatenate_elements(()), ())
        self.assertEqual(concatenate_elements((1)), ())

import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertIsInstance(concatenate_elements(()), tuple)
        self.assertIsInstance(concatenate_elements((1,)), tuple)

    def test_single_element_tuple(self):
        self.assertIsInstance(concatenate_elements((1,)), tuple)
        self.assertEqual(concatenate_elements((1,)), (1,))

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(concatenate_elements((1, 2, 3)), tuple)
        self.assertEqual(concatenate_elements((1, 2, 3)), (1+2, 2+3))

    def test_mixed_types(self):
        self.assertIsInstance(concatenate_elements((1, 'a')), tuple)
        self.assertNotEqual(concatenate_elements((1, 'a')), (1+'a'))

    def test_negative_numbers(self):
        self.assertIsInstance(concatenate_elements((-1, 2)), tuple)
        self.assertEqual(concatenate_elements((-1, 2)), (-1+2, 2))

    def test_empty_second_half(self):
        self.assertIsInstance(concatenate_elements((1,)), tuple)
        self.assertIsInstance(concatenate_elements((1,)), tuple)

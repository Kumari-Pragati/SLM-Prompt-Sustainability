import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(concatenate_elements([1, 2, 3]), '1 2 3')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements([4]), '4')

    def test_negative_numbers(self):
        self.assertEqual(concatenate_elements([-1, -2, -3]), '-1 -2 -3')

    def test_mixed_types(self):
        self.assertEqual(concatenate_elements([1, 'a', 2]), '1 a 2')

    def test_large_numbers(self):
        self.assertEqual(concatenate_elements([1000000, 2000000, 3000000]), '1000000 2000000 3000000')

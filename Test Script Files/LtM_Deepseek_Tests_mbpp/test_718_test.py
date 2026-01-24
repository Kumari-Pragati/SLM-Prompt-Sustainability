import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(alternate_elements([]), [])

    def test_single_element_list(self):
        self.assertEqual(alternate_elements([1]), [1])

    def test_duplicate_elements_list(self):
        self.assertEqual(alternate_elements([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(alternate_elements([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_mixed_numbers(self):
        self.assertEqual(alternate_elements([1, -2, 3, -4, 5]), [1, 3, 5])

import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(alternate_elements([]), [])

    def test_single_element(self):
        self.assertEqual(alternate_elements([1]), [1])

    def test_two_elements(self):
        self.assertEqual(alternate_elements([1, 2]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(alternate_elements([1, 1, 2, 2]), [1, 2])

    def test_negative_numbers(self):
        self.assertEqual(alternate_elements([-1, -2, -3, -4]), [-1, -3])

    def test_zero(self):
        self.assertEqual(alternate_elements([0, 1, 2, 3]), [0, 2])

    def test_large_numbers(self):
        self.assertEqual(alternate_elements(list(range(1, 101))), list(range(1, 101, 2)))

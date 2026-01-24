import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(alternate_elements([]), [])

    def test_single_element(self):
        self.assertListEqual(alternate_elements([1]), [1])

    def test_even_length(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_odd_length(self):
        self.assertListEqual(alternate_elements([1, 2, 3]), [1, 3])

    def test_first_element_is_odd(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_first_element_is_even(self):
        self.assertListEqual(alternate_elements([2, 3, 4, 5]), [2, 4])

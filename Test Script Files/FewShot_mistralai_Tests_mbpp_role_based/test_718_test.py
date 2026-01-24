import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(alternate_elements([]), [])

    def test_single_element_list(self):
        self.assertListEqual(alternate_elements([1]), [1])

    def test_even_length_list(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_odd_length_list(self):
        self.assertListEqual(alternate_elements([1, 2, 3]), [1, 3])

    def test_list_with_duplicates(self):
        self.assertListEqual(alternate_elements([1, 2, 1, 3]), [1, 1, 3])

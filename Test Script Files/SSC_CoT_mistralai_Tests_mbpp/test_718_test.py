import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3])
        self.assertListEqual(alternate_elements([7, 8, 9, 10, 11]), [7, 9])

    def test_empty_list(self):
        self.assertListEqual(alternate_elements([]), [])

    def test_single_element(self):
        self.assertListEqual(alternate_elements([1]), [1])

    def test_odd_length(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_even_length(self):
        self.assertListEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3])

    def test_negative_numbers(self):
        self.assertListEqual(alternate_elements([-1, 2, -3, 4]), [-1, 4])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            alternate_elements([1, 2, "three", 4])

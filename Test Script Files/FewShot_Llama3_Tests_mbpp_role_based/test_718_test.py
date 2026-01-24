import unittest
from mbpp_718_code import alternate_elements

class TestAlternateElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(alternate_elements([]), [])

    def test_single_element_list(self):
        self.assertEqual(alternate_elements([1]), [])

    def test_list_with_even_number_of_elements(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4]), [1, 3])

    def test_list_with_odd_number_of_elements(self):
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_list_with_non_integer_elements(self):
        self.assertEqual(alternate_elements(['a', 'b', 'c', 'd']), ['a', 'c'])

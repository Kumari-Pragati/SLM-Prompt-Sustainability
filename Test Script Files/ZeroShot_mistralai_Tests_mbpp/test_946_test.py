import unittest
from mbpp_946_code import Counter
from your_module import most_common_elem  # replace 'your_module' with the actual module name where the function is defined

class TestMostCommonElem(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(most_common_elem([], 1), [])

    def test_single_element(self):
        self.assertEqual(most_common_elem([1], 1), [(1, 1)])

    def test_multiple_elements(self):
        self.assertEqual(most_common_elem([1, 2, 1, 3, 2, 2], 2), [(2, 3)])

    def test_multiple_elements_tie(self):
        self.assertEqual(most_common_elem([1, 2, 1, 3, 2, 2, 1], 3), [(1, 2), (2, 2)])

    def test_more_elements_than_requested(self):
        self.assertEqual(most_common_elem([1, 2, 1, 3, 2, 2], 1), [(2, 2)])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            most_common_elem([1, 2, 1], -1)

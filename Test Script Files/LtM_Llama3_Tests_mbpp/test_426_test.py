import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_single_element(self):
        self.assertEqual(filter_oddnumbers([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(filter_oddnumbers([-1, -2, -3, -4, -5]), [-1, -3, -5])

    def test_mixed_numbers(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            filter_oddnumbers(['a', 'b', 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            filter_oddnumbers(123)

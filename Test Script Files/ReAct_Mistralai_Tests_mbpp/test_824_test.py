import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_even([]), [])

    def test_single_element(self):
        self.assertListEqual(remove_even([1]), [1])
        self.assertListEqual(remove_even([2]), [])

    def test_even_length(self):
        self.assertListEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertListEqual(remove_even([2, 4, 6, 8]), [6, 8])

    def test_odd_length(self):
        self.assertListEqual(remove_even([1, 2, 3, 4]), [1, 3])
        self.assertListEqual(remove_even([2, 4, 6, 8, 10]), [10])

    def test_list_with_duplicates(self):
        self.assertListEqual(remove_even([1, 2, 2, 3, 4, 4, 5]), [1, 3, 5])

    def test_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            remove_even([1, 'two', 3])

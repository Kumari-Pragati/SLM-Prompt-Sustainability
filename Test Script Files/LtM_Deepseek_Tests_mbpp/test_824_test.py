import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(remove_even([1, 2, 3, 4]), [1, 3])

    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_all_even_list(self):
        self.assertEqual(remove_even([2, 4, 6]), [])

    def test_all_odd_list(self):
        self.assertEqual(remove_even([1, 3, 5]), [1, 3, 5])

    def test_mixed_list(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_element_list(self):
        self.assertEqual(remove_even([2]), [])

    def test_single_element_odd_list(self):
        self.assertEqual(remove_even([1]), [1])

import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_odd([2]), [2])

    def test_all_odd(self):
        self.assertEqual(remove_odd([1, 3, 5, 7, 9]), [])

    def test_all_even(self):
        self.assertEqual(remove_odd([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_mixed_list(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_odd([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]), [2, 2, 4, 4, 6, 6, 8, 8, 10])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_odd('test')

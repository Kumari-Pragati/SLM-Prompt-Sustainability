import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_remove_odd_typical(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_remove_odd_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_remove_odd_single_element(self):
        self.assertEqual(remove_odd([1]), [])

    def test_remove_odd_all_odd(self):
        self.assertEqual(remove_odd([1, 3, 5, 7, 9]), [])

    def test_remove_odd_all_even(self):
        self.assertEqual(remove_odd([2, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

    def test_remove_odd_mixed(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10])

    def test_remove_odd_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_odd('hello')

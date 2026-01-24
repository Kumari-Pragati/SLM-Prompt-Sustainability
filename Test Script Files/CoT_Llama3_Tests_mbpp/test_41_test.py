import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_evennumbers([]), [])

    def test_single_even(self):
        self.assertEqual(filter_evennumbers([2]), [2])

    def test_single_odd(self):
        self.assertEqual(filter_evennumbers([3]), [])

    def test_multiple_even(self):
        self.assertEqual(filter_evennumbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_multiple_odd(self):
        self.assertEqual(filter_evennumbers([1, 3, 5, 7]), [])

    def test_mixed(self):
        self.assertEqual(filter_evennumbers([2, 3, 4, 5, 6, 7, 8]), [2, 4, 6, 8])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            filter_evennumbers(['a', 'b', 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            filter_evennumbers(123)

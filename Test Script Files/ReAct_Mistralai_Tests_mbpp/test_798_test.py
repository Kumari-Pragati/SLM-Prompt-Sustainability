import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_empty_list(self):
        """Tests sum function with an empty list"""
        self.assertEqual(_sum([]), 0)

    def test_single_element_list(self):
        """Tests sum function with a single element list"""
        self.assertEqual(_sum([1]), 1)

    def test_positive_numbers_list(self):
        """Tests sum function with a list of positive numbers"""
        self.assertEqual(_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers_list(self):
        """Tests sum function with a list of negative numbers"""
        self.assertEqual(_sum([-1, -2, -3, -4, -5]), 15)

    def test_mixed_numbers_list(self):
        """Tests sum function with a list of mixed numbers"""
        self.assertEqual(_sum([1, -2, 3, -4, 5]), 6)

    def test_large_numbers_list(self):
        """Tests sum function with a large list of numbers"""
        large_list = [i for i in range(1000)]
        self.assertEqual(_sum(large_list), sum(large_list))

    def test_list_with_zero(self):
        """Tests sum function with a list containing zero"""
        self.assertEqual(_sum([0, 1, 2, 3, 4]), 10)

    def test_list_with_duplicates(self):
        """Tests sum function with a list containing duplicates"""
        self.assertEqual(_sum([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 25)

    def test_list_with_floats(self):
        """Tests sum function with a list containing floats"""
        self.assertEqual(_sum([1.1, 2.2, 3.3]), 6.6)

    def test_list_with_strings(self):
        """Tests sum function with a list containing strings"""
        self.assertEqual(_sum(["1", "2", "3"]), 6)

    def test_list_with_none(self):
        """Tests sum function with a list containing None"""
        self.assertEqual(_sum([None, 1, 2, 3]), 6)

    def test_list_with_empty_tuple(self):
        """Tests sum function with a list containing an empty tuple"""
        self.assertEqual(_sum([(1,), 1, 2, 3]), 6)

    def test_list_with_error(self):
        """Tests sum function with a list containing an error"""
        with self.assertRaises(TypeError):
            _sum([1, "2", 3])

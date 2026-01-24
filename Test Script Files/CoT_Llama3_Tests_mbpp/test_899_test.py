import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_positive_array(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_negative_array(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_positive_and_negative_array(self):
        self.assertTrue(check([1, -2, 3, -4, 5], 5))

    def test_array_with_duplicates(self):
        self.assertTrue(check([1, 2, 2, 3, 4, 5], 6))

    def test_array_with_negative_duplicates(self):
        self.assertTrue(check([-1, -2, -2, -3, -4, -5], 6))

    def test_array_with_no_elements(self):
        self.assertTrue(check([], 0))

    def test_array_with_one_element(self):
        self.assertTrue(check([1], 1))

    def test_array_with_two_elements(self):
        self.assertTrue(check([1, 2], 2))

    def test_array_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            check([1, 2, 3, '4', 5], 5)

    def test_array_with_non_integer_elements_and_duplicates(self):
        with self.assertRaises(TypeError):
            check([1, 2, 2, '3', 4, 5], 6)

    def test_array_with_non_integer_elements_and_negative_duplicates(self):
        with self.assertRaises(TypeError):
            check([-1, -2, -2, '3', -4, -5], 6)

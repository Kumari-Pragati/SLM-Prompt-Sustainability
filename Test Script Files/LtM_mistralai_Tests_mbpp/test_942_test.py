import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_empty_input(self):
        self.assertFalse(check_element((), []))
        self.assertFalse(check_element((), [1, 2, 3]))
        self.assertFalse(check_element([], []))
        self.assertFalse(check_element([1, 2, 3], ()))

    def test_single_element(self):
        self.assertTrue(check_element((1,), [1]))
        self.assertFalse(check_element((2,), [1]))

    def test_multiple_elements(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3, 4]))
        self.assertFalse(check_element((1, 2, 3), [4, 5, 6]))

    def test_negative_numbers(self):
        self.assertTrue(check_element((-1, 0, 1), [-1, 0, 1]))
        self.assertFalse(check_element((-1, 0, 1), [2, 3, 4]))

    def test_zero(self):
        self.assertTrue(check_element((0,), [0]))
        self.assertFalse(check_element((0,), [1]))

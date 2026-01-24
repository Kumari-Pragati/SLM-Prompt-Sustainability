import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(right_insertion([1, 3, 5], 2), 2)
        self.assertEqual(right_insertion([1, 3, 5], 4), 3)
        self.assertEqual(right_insertion([1, 3, 5], 6), 4)

    def test_zero(self):
        self.assertEqual(right_insertion([0], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(right_insertion([-1, -3, -5], -2), 3)
        self.assertEqual(right_insertion([-1, -3, -5], -4), 4)
        self.assertEqual(right_insertion([-1, -3, -5], -6), 4)

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(right_insertion([1], 1), 1)
        self.assertEqual(right_insertion([-1], -1), 1)

    def test_duplicate_elements(self):
        self.assertEqual(right_insertion([1, 1, 3, 5], 1), 2)
        self.assertEqual(right_insertion([1, 1, 3, 5], 3), 3)
        self.assertEqual(right_insertion([1, 1, 3, 5], 5), 4)

    def test_floats(self):
        self.assertEqual(right_insertion([1.0, 3.0, 5.0], 2.0), 3)
        self.assertEqual(right_insertion([1.0, 3.0, 5.0], 4.0), 4)
        self.assertEqual(right_insertion([1.0, 3.0, 5.0], 6.0), 4)

    def test_negative_floats(self):
        self.assertEqual(right_insertion([-1.0, -3.0, -5.0], -2.0), 3)
        self.assertEqual(right_insertion([-1.0, -3.0, -5.0], -4.0), 4)
        self.assertEqual(right_insertion([-1.0, -3.0, -5.0], -6.0), 4)

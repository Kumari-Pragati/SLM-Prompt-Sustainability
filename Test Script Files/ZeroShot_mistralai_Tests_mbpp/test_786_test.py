import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 3), 0)

    def test_single_element(self):
        self.assertEqual(right_insertion([1], 3), 1)
        self.assertEqual(right_insertion([3], 3), 0)

    def test_multiple_elements(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 3)
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(right_insertion([6, 5, 4, 3, 2, 1], 3), 4)

    def test_negative_numbers(self):
        self.assertEqual(right_insertion([-1, -2, -3, -4, -5], -3), 3)
        self.assertEqual(right_insertion([-6, -5, -4, -3, -2, -1], -3), 4)

    def test_floats(self):
        self.assertEqual(right_insertion([1.1, 2.2, 3.3], 2.2), 2)
        self.assertEqual(right_insertion([3.3, 2.2, 1.1], 2.2), 2)

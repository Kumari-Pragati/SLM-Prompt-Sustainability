import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(right_insertion([], 3), 0)

    def test_single_element_list(self):
        self.assertEqual(right_insertion([1], 1), 0)
        self.assertEqual(right_insertion([1], 2), 1)

    def test_multiple_elements_left(self):
        self.assertEqual(right_insertion([1, 2, 3], 0), 3)
        self.assertEqual(right_insertion([1, 2, 3], 1), 0)
        self.assertEqual(right_insertion([1, 2, 3], 2), 1)
        self.assertEqual(right_insertion([1, 2, 3], 4), 4)

    def test_multiple_elements_right(self):
        self.assertEqual(right_insertion([3, 2, 1], 4), 4)
        self.assertEqual(right_insertion([3, 2, 1], 3), 2)
        self.assertEqual(right_insertion([3, 2, 1], 2), 1)
        self.assertEqual(right_insertion([3, 2, 1], 1), 0)

    def test_equal_elements(self):
        self.assertEqual(right_insertion([3, 3, 3], 3), 0)

    def test_negative_numbers(self):
        self.assertEqual(right_insertion([3, 2, -1], -2), 3)

    def test_floats(self):
        self.assertEqual(right_insertion([3, 2.5, 1], 3), 0)
        self.assertEqual(right_insertion([3, 2.5, 1], 2.5), 1)
        self.assertEqual(right_insertion([3, 2.5, 1], 1), 2)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            right_insertion(1.23, "x")

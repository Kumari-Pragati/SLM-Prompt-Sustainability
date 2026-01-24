import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_single_element_list(self):
        self.assertEqual(left_insertion([3], 5), 1)
        self.assertEqual(left_insertion([3], 3), 0)

    def test_multiple_elements_ascending(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 2), 1)
        self.assertEqual(left_insertion([1, 3, 5, 7], 1), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 8), 4)

    def test_multiple_elements_descending(self):
        self.assertEqual(left_insertion([7, 5, 3, 1], 2), 1)
        self.assertEqual(left_insertion([7, 5, 3, 1], 7), 0)
        self.assertEqual(left_insertion([7, 5, 3, 1], -1), 0)

    def test_duplicate_values(self):
        self.assertEqual(left_insertion([1, 1, 3, 5, 5], 1), 0)
        self.assertEqual(left_insertion([1, 1, 3, 5, 5], 5), 2)

    def test_floats(self):
        self.assertEqual(left_insertion([1.0, 3.0, 5.0], 2.0), 1)
        self.assertEqual(left_insertion([1.0, 3.0, 5.0], 1.0), 0)
        self.assertEqual(left_insertion([1.0, 3.0, 5.0], 4.0), 3)

    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-3, -1, 1], -2), 0)
        self.assertEqual(left_insertion([-3, -1, 1], -3), 0)
        self.assertEqual(left_insertion([-3, -1, 1], -1), 1)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            left_insertion([1, 3, 5], "not_a_number")

import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(right_insertion([], 3), 0)

    def test_single_element_list(self):
        self.assertEqual(right_insertion([1], 1), 0)
        self.assertEqual(right_insertion([1], 2), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(right_insertion([1, 2, 3], 1), 0)
        self.assertEqual(right_insertion([1, 2, 3], 2), 1)
        self.assertEqual(right_insertion([1, 2, 3], 3), 2)
        self.assertEqual(right_insertion([1, 2, 3], 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(right_insertion([3, 2, 1], -1), 0)
        self.assertEqual(right_insertion([3, 2, 1], -2), 0)
        self.assertEqual(right_insertion([3, 2, 1], -3), 3)

    def test_floats(self):
        self.assertEqual(right_insertion([1.0, 2.0, 3.0], 1.5), 2)

    def test_duplicates(self):
        self.assertEqual(right_insertion([1, 1, 2, 3], 1), 2)

    def test_bisect_right_behavior(self):
        self.assertEqual(right_insertion([3, 2, 1], 2), bisect.bisect_right([3, 2, 1], 2))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, right_insertion, [], 'x')
        self.assertRaises(TypeError, right_insertion, [1], 3.0)

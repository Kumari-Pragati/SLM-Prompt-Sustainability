import unittest
from mbpp_517_code import largest_pos

class TestLargestPos(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(largest_pos([]), None)

    def test_single_element_list(self):
        self.assertEqual(largest_pos([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(largest_pos([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(largest_pos([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_pos([1, -2, 3, -4, 5]), 5)

    def test_duplicates(self):
        self.assertEqual(largest_pos([1, 1, 2, 1, 3]), 3)

    def test_floats(self):
        self.assertEqual(largest_pos([1.1, 2.2, 3.3]), 3.3)

    def test_invalid_input(self):
        self.assertRaises(TypeError, largest_pos, "string")

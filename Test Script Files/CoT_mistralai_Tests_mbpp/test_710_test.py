import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(front_and_rear([]))

    def test_single_element_list(self):
        self.assertEqual(front_and_rear([1]), (1,))

    def test_multiple_elements_list(self):
        self.assertEqual(front_and_rear([1, 2, 3]), (1, 3))

    def test_negative_index(self):
        self.assertRaises(IndexError, front_and_rear, [1, 2, 3], -1)

    def test_string_input(self):
        self.assertRaises(TypeError, front_and_rear, "abc")

    def test_mixed_type_input(self):
        self.assertRaises(TypeError, front_and_rear, [1, "a", 2])

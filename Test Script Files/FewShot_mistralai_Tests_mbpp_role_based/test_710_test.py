import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(front_and_rear([]))

    def test_single_element_list(self):
        self.assertEqual(front_and_rear([1]), (1, 1))

    def test_normal_list(self):
        self.assertEqual(front_and_rear([1, 2, 3]), (1, 3))

    def test_list_with_duplicates(self):
        self.assertEqual(front_and_rear([1, 1, 2, 3]), (1, 3))

    def test_list_with_negative_numbers(self):
        self.assertEqual(front_and_rear([-1, 0, 1]), (-1, 1))

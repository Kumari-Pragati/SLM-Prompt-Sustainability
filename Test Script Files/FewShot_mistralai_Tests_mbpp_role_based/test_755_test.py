import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_single_element(self):
        self.assertIsNone(second_smallest([1]))

    def test_two_equal_elements(self):
        self.assertIsNone(second_smallest([2, 2]))

    def test_two_different_elements(self):
        self.assertEqual(second_smallest([1, 2]), 1)

    def test_three_elements_ascending(self):
        self.assertEqual(second_smallest([1, 2, 3]), 2)

    def test_three_elements_descending(self):
        self.assertEqual(second_smallest([3, 2, 1]), 2)

    def test_three_elements_duplicate(self):
        self.assertEqual(second_smallest([1, 1, 2]), 2)

    def test_four_elements_ascending(self):
        self.assertEqual(second_smallest([1, 2, 3, 4]), 2)

    def test_four_elements_descending(self):
        self.assertEqual(second_smallest([4, 3, 2, 1]), 2)

    def test_four_elements_duplicate(self):
        self.assertEqual(second_smallest([1, 1, 2, 2]), 1)

    def test_empty_list(self):
        self.assertIsNone(second_smallest([]))

import unittest
from790_code import even_position

class TestEvenPosition(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(even_position([]))

    def test_single_element(self):
        for num in [0, 1]:
            self.assertTrue(even_position([num]))

    def test_even_length(self):
        for nums in [
            [0, 2, 4, 6],
            [1, 3, 5, 7],
            [2, 4, 0, 6],
            [3, 5, 1, 7],
        ]:
            self.assertTrue(even_position(nums))

    def test_odd_length(self):
        for nums in [
            [0, 2, 4, 6, 8],
            [1, 3, 5, 7, 9],
            [2, 4, 0, 6, 8],
            [3, 5, 1, 7, 9],
        ]:
            self.assertFalse(even_position(nums))

    def test_invalid_input(self):
        self.assertRaises(TypeError, even_position, "not a list")

import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(remove(['a', 'b', '1', 'c', '2', 'd']), ['a', 'b', 'c', 'd'])

    def test_empty_input(self):
        self.assertListEqual(remove([]), [])

    def test_single_input(self):
        self.assertListEqual(remove(['1']), [])

    def test_all_digits_input(self):
        self.assertListEqual(remove([1, 2, 3]), [])

    def test_mixed_input(self):
        self.assertListEqual(remove(['a1b2c3']), ['a', 'b', 'c'])

    def test_special_characters(self):
        self.assertListEqual(remove(['a#1b2c3$']), ['a', '#', 'b', '2', 'c', '$'])

    def test_negative_numbers(self):
        self.assertListEqual(remove([-1, -2, -3]), [])

import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(remove(['a', '1b', '2c', '3d']), ['a', 'b', 'c', 'd'])

    def test_empty_input(self):
        self.assertListEqual(remove([]), [])

    def test_single_input(self):
        self.assertListEqual(remove(['abc123']), ['abc'])

    def test_negative_numbers(self):
        self.assertListEqual(remove(['-1', '-2', '-3']), ['-'])

    def test_special_characters(self):
        self.assertListEqual(remove(['a#1b$2c%3d', 'eFg4hIj5kLm6nO']),
                              ['a#b$c%', 'eFg4hIj5kLm6nO'])

    def test_mixed_input(self):
        self.assertListEqual(remove(['a1b2c3d4', 'e5f6g7h8i9j0']),
                              ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

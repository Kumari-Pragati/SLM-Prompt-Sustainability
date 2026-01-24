import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove([]), [])

    def test_single_element_list(self):
        self.assertListEqual(remove(['a']), ['a'])

    def test_list_with_numbers(self):
        self.assertListEqual(remove(['a1b2c3', 'd4e5f6']), ['aebcf', 'de'])

    def test_list_with_only_numbers(self):
        self.assertListEqual(remove([1, 2, 3, 4, 5]), [])

    def test_list_with_mixed_types(self):
        self.assertListEqual(remove(['a1b2c3', 4, 'd5e6f7', 8]), ['aebcf', None, 'de', None])

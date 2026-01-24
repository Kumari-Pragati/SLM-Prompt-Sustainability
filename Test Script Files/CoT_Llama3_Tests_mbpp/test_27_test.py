import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_remove_numbers(self):
        self.assertEqual(remove(['hello1', 'world2', 'python3']), ['hello', 'world', 'python'])

    def test_remove_numbers_multiple(self):
        self.assertEqual(remove(['hello1', 'world2', 'python3', 'abc4', 'def5']), ['hello', 'world', 'python', 'abc', 'def'])

    def test_remove_numbers_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_remove_numbers_single_element(self):
        self.assertEqual(remove(['hello']), ['hello'])

    def test_remove_numbers_empty_string(self):
        self.assertEqual(remove(['hello', '']), ['hello'])

    def test_remove_numbers_invalid_input(self):
        with self.assertRaises(TypeError):
            remove(None)

    def test_remove_numbers_non_list_input(self):
        with self.assertRaises(TypeError):
            remove('hello')

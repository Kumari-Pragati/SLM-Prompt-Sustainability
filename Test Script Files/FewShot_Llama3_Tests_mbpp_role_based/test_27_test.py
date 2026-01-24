import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_remove_numbers_from_list(self):
        list_to_remove = ['1', '2', '3', '4', '5']
        result = remove(list_to_remove)
        self.assertEqual(result, ['', '', '', '', ''])

    def test_remove_numbers_from_empty_list(self):
        list_to_remove = []
        result = remove(list_to_remove)
        self.assertEqual(result, [])

    def test_remove_numbers_from_list_with_non_numbers(self):
        list_to_remove = ['1', 'hello', '2', 'world', '3']
        result = remove(list_to_remove)
        self.assertEqual(result, ['', 'hello', '', 'world', ''])

    def test_remove_numbers_from_list_with_mixed_case(self):
        list_to_remove = ['1', 'HeLlO', '2', 'WoRlD', '3']
        result = remove(list_to_remove)
        self.assertEqual(result, ['', 'HeLlO', '', 'WoRlD', ''])

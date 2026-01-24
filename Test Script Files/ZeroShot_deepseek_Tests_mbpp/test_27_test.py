import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):

    def test_remove_numbers(self):
        self.assertEqual(remove(['1apple', '2banana', '3cherry']), ['apple', 'banana', 'cherry'])
        self.assertEqual(remove(['4orange', '5kiwi', '6mango']), ['orange', 'kiwi', 'mango'])
        self.assertEqual(remove(['7grape', '8pear', '9peach']), ['grape', 'pear', 'peach'])

    def test_remove_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_remove_no_numbers(self):
        self.assertEqual(remove(['apple', 'banana', 'cherry']), ['apple', 'banana', 'cherry'])

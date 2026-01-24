import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_single_element(self):
        self.assertEqual(second_frequent(['a']), None)

    def test_two_elements(self):
        self.assertEqual(second_frequent(['a', 'a']), 'a')
        self.assertEqual(second_frequent(['a', 'b']), None)

    def test_multiple_elements(self):
        self.assertEqual(second_frequent(['a', 'b', 'a', 'b', 'c', 'a']), 'a')

    def test_duplicate_values(self):
        self.assertEqual(second_frequent([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]), 4)

    def test_large_input(self):
        large_input = [i for i in range(1000)]
        self.assertEqual(second_frequent(large_input), large_input[1])

    def test_negative_numbers(self):
        self.assertEqual(second_frequent([-1, -1, 0, 0, 1, 1]), 0)

    def test_string_input(self):
        self.assertEqual(second_frequent(list('aaabbbccc')), 'b')

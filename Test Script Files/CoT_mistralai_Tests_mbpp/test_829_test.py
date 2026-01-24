import unittest
from mbpp_829_code import Counter
from copy import deepcopy

class TestSecondFrequent(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(second_frequent([]))

    def test_single_element(self):
        self.assertIsNone(second_frequent([1]))

    def test_two_elements(self):
        self.assertEqual(second_frequent([1, 1]), 1)
        self.assertEqual(second_frequent([2, 1]), 1)

    def test_multiple_elements(self):
        data = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5]
        self.assertEqual(second_frequent(data), 2)

    def test_duplicate_second_frequent(self):
        data = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5]
        self.assertIsNone(second_frequent(data))

    def test_invalid_input(self):
        self.assertRaises(TypeError, second_frequent, (1, 2, 3))
        self.assertRaises(TypeError, second_frequent, [1, '2', 3])
        self.assertRaises(TypeError, second_frequent, [1, 2, '3'])

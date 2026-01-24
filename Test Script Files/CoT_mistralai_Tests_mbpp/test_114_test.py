import unittest
from mbpp_114_code import Counter
from 114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), '[]')

    def test_single_element(self):
        self.assertEqual(assign_freq([1]), '[1: 1]')

    def test_multiple_elements(self):
        self.assertEqual(assign_freq([1, 2, 1, 3, 2, 1]), '[1: 3, 2: 2, 3: 1]')

    def test_duplicate_elements(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3, 2, 2, 1, 1]), '[1: 4, 2: 4, 3: 2]')

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([1, -1, 2, -2, 3, -3]), '[1: 1, -1: 1, 2: 1, -2: 1, 3: 1, -3: 1]')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            assign_freq([1, 'a', 2])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            assign_freq('invalid input')

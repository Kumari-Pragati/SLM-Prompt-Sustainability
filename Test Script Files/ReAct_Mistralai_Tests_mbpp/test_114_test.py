import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), '[]')

    def test_single_element(self):
        self.assertEqual(assign_freq([1]), '[1: 1]')

    def test_multiple_elements(self):
        self.assertEqual(assign_freq([1, 2, 1, 3, 2, 2]),
                         '[1: 2, 2: 3, 3: 1]')

    def test_duplicate_elements(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3, 3]),
                         '[1: 2, 2: 2, 3: 3]')

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -2, -1, 0, 1]),
                         '[-1: 2, 0: 1, 1: 1]')

    def test_zero(self):
        self.assertEqual(assign_freq([0]), '[0: 1]')

    def test_large_numbers(self):
        self.assertEqual(assign_freq([1000000, 1000000, 1000001]),
                         '[1000000: 2, 1000001: 1]')

    def test_floats(self):
        self.assertEqual(assign_freq([1.1, 1.2, 1.3]),
                         '[1.1: 1, 1.2: 1, 1.3: 1]')

    def test_strings(self):
        self.assertEqual(assign_freq(['a', 'a', 'b', 'b', 'c']),
                         '["a": 2, "b": 2, "c": 1]')

    def test_mixed_types(self):
        self.assertEqual(assign_freq([1, 'a', 2, 'a', 3]),
                         '[1: 1, "a": 2, 2: 1, 3: 1]')

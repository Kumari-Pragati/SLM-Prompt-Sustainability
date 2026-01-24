import unittest
from mbpp_41_code import filter_evennumbers

class TestFilterEvenNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], filter_evennumbers([]))

    def test_single_number(self):
        self.assertListEqual([2], filter_evennumbers([2]))
        self.assertListEqual([], filter_evennumbers([1]))

    def test_multiple_numbers(self):
        self.assertListEqual([2, 4, 6], filter_evennumbers([2, 4, 6, 1, 3]))
        self.assertListEqual([4, 6, 8], filter_evennumbers([4, 6, 8, 1, 3]))

    def test_negative_numbers(self):
        self.assertListEqual([-2, -4, -6], filter_evennumbers([-2, -4, -6, -1, 0]))
        self.assertListEqual([], filter_evennumbers([-1, 0]))

    def test_floats(self):
        self.assertListEqual([2.0], filter_evennumbers([2.0]))
        self.assertListEqual([], filter_evennumbers([1.5]))

    def test_strings(self):
        self.assertListEqual([], filter_evennumbers(["a", "b", "c"]))

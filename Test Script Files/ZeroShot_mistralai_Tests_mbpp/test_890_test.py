import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_find_extra_empty_arrays(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_find_extra_same_arrays(self):
        self.assertEqual(find_Extra([1, 2, 3], [1, 2, 3], 3), 3)

    def test_find_extra_single_extra(self):
        self.assertEqual(find_Extra([1, 1, 2], [1, 2, 2], 3), 1)

    def test_find_extra_multiple_extras(self):
        self.assertEqual(find_Extra([1, 1, 2, 3], [1, 2, 4, 3], 4), 2)

    def test_find_extra_out_of_range_index(self):
        self.assertEqual(find_Extra([1, 1, 2], [1, 2, 2], 4), 3)

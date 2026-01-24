import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_identical([], []))
        self.assertTrue(check_identical([1.0, 2.0, 3.0], [1, 2, 3]))

    def test_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))
        self.assertFalse(check_identical([1, 2, 3], [1, 2, 3, 4]))

    def test_different_elements(self):
        self.assertFalse(check_identical([1, 2, 3], [2, 2, 3]))
        self.assertFalse(check_identical([1, 2, 3], [1, 3, 3]))

    def test_mixed_types(self):
        self.assertFalse(check_identical([1, 2, 3], [1, '2', 3]))
        self.assertFalse(check_identical([1, 2, 3], [1, 2, '3']))

    def test_empty_inputs(self):
        self.assertRaises(TypeError, check_identical, [], None)
        self.assertRaises(TypeError, check_identical, [1], None)

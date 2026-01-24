import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_different_order(self):
        self.assertTrue(check_identical([1, 2, 3], [3, 2, 1]))

    def test_different_elements(self):
        self.assertFalse(check_identical([1, 2, 3], [4, 5, 6]))

    def test_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_single_element(self):
        self.assertTrue(check_identical([1], [1]))

    def test_none_inputs(self):
        with self.assertRaises(TypeError):
            check_identical(None, [1, 2, 3])
        with self.assertRaises(TypeError):
            check_identical([1, 2, 3], None)

    def test_mixed_type_inputs(self):
        self.assertFalse(check_identical([1, '2', 3], [1, 2, 3]))

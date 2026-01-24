import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([1, 2, 3]))
        self.assertFalse(empty_dit(["a", "b", "c"]))
        self.assertFalse(empty_dit([1.0, 2.0, 3.0]))

    def test_single_element_list(self):
        self.assertTrue(empty_dit([]))
        self.assertFalse(empty_dit([0]))
        self.assertFalse(empty_dit([0.0]))
        self.assertFalse(empty_dit(["a"]))

    def test_empty_string(self):
        self.assertTrue(empty_dit([]))
        self.assertTrue(empty_dit(""))

    def test_invalid_input(self):
        self.assertRaises(TypeError, empty_dit, 123)
        self.assertRaises(TypeError, empty_dit, (1, 2, 3))
        self.assertRaises(TypeError, empty_dit, {"key": "value"})

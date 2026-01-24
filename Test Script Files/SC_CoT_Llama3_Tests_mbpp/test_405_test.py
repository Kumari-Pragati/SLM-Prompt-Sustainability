import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    def test_typical_true(self):
        self.assertTrue(check_tuplex([1, 2, 3], [1, 2, 3]))

    def test_typical_false(self):
        self.assertFalse(check_tuplex([1, 2, 3], [4, 5, 6]))

    def test_edge_empty_tuplex(self):
        self.assertFalse(check_tuplex([], [1, 2, 3]))

    def test_edge_empty_tuple1(self):
        self.assertFalse(check_tuplex([1, 2, 3], []))

    def test_edge_single_element_tuplex(self):
        self.assertTrue(check_tuplex([1], [1]))

    def test_edge_single_element_tuple1(self):
        self.assertFalse(check_tuplex([1, 2, 3], [1]))

    def test_edge_tuplex_subset_of_tuple1(self):
        self.assertTrue(check_tuplex([1, 2], [1, 2, 3]))

    def test_edge_tuple1_subset_of_tuplex(self):
        self.assertFalse(check_tuplex([1, 2, 3], [1, 2]))

    def test_invalid_input_non_iterable_tuplex(self):
        with self.assertRaises(TypeError):
            check_tuplex("string", [1, 2, 3])

    def test_invalid_input_non_iterable_tuple1(self):
        with self.assertRaises(TypeError):
            check_tuplex([1, 2, 3], "string")

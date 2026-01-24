import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(0), [])

    def test_single_element_list(self):
        self.assertEqual(empty_list(1), [{},])

    def test_multiple_element_list(self):
        self.assertEqual(empty_list(5), [{}, {}, {}, {}, {}])

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            empty_list(-1)

    def test_non_integer_length(self):
        with self.assertRaises(TypeError):
            empty_list("five")

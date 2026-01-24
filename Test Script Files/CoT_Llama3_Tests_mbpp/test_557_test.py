import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")

    def test_edge_case1(self):
        self.assertEqual(toggle_string(""), "")

    def test_edge_case2(self):
        self.assertEqual(toggle_string("abc"), "ABC")

    def test_edge_case3(self):
        self.assertEqual(toggle_string("ABC"), "abc")

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            toggle_string(123)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            toggle_string([1, 2, 3])

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            toggle_string(None)

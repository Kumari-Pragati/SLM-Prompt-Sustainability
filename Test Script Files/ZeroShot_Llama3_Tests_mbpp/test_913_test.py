import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_end_num_positive(self):
        self.assertTrue(end_num("Hello123"))
        self.assertTrue(end_num("World456"))
        self.assertTrue(end_num("Python789"))

    def test_end_num_negative(self):
        self.assertFalse(end_num("Hello"))
        self.assertFalse(end_num("World"))
        self.assertFalse(end_num("Python"))

    def test_end_num_edge_case(self):
        self.assertTrue(end_num("123Hello"))
        self.assertTrue(end_num("456World"))
        self.assertTrue(end_num("789Python"))

    def test_end_num_empty_string(self):
        self.assertFalse(end_num(""))

    def test_end_num_non_string_input(self):
        with self.assertRaises(TypeError):
            end_num(123)

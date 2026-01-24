import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(reverse_string_list(["hello", "world"]), ["olleh", "dlrow"])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(reverse_string_list([""]), [""])
        self.assertEqual(reverse_string_list(["a"]), ["a"])
        self.assertEqual(reverse_string_list(["abc", "def", "ghi"]), ["cba", "fed", "ihg"])
        self.assertEqual(reverse_string_list(["z", "y", "x"]), ["x", "y", "z"])

    def test_special_input(self):
        self.assertEqual(reverse_string_list(["Python", "Programming", "is", "fun"]), ["notu si", "gnimargorp", "mom yliP", "nohtyP"])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_string_list(123)
        with self.assertRaises(TypeError):
            reverse_string_list([])

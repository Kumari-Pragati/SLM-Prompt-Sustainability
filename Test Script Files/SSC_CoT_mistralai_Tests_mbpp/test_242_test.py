import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_charac("hello"), 5)
        self.assertEqual(count_charac("Python"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_charac(""), 0)
        self.assertEqual(count_charac("a" * 10000), 10000)
        self.assertEqual(count_charac("a\nb"), 2)

    def test_special_cases(self):
        self.assertEqual(count_charac("\t"), 1)
        self.assertEqual(count_charac("a\u200b"), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_charac, 123)
        self.assertRaises(TypeError, count_charac, (1, 2, 3))

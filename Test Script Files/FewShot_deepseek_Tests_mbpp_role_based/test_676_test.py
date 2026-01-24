import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_extra_char('Hello, World!'), 'HelloWorld')

    def test_edge_condition(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_extra_char('a' * 10000), 'a' * 10000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_extra_char(12345)

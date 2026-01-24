import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_extra_char('Hello World'), 'HelloWorld')
        self.assertEqual(remove_extra_char('Hello_World'), 'HelloWorld')
        self.assertEqual(remove_extra_char('Hello123'), 'Hello123')

    def test_edge(self):
        self.assertEqual(remove_extra_char(''), '')
        self.assertEqual(remove_extra_char('Hello'), 'Hello')
        self.assertEqual(remove_extra_char('123'), '123')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_extra_char(None)
        with self.assertRaises(TypeError):
            remove_extra_char(123)

import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char('hello', 'l'), 5)

    def test_edge_case(self):
        self.assertEqual(last_occurence_char('a', 'a'), 2)
        self.assertEqual(last_occurence_char('abc', 'd'), None)

    def test_boundary_case(self):
        self.assertEqual(last_occurence_char('', 'a'), None)
        self.assertEqual(last_occurence_char('a', ''), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            last_occurence_char(123, 'a')
        with self.assertRaises(TypeError):
            last_occurence_char('hello', 123)

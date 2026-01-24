import unittest
from mbpp_604_code import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(reverse_words('Hello World'), 'World Hello')
        self.assertEqual(reverse_words('Python is fun'), 'fun is Python')

    def test_edge_conditions(self):
        self.assertEqual(reverse_words(''), '')
        self.assertEqual(reverse_words('     '), '     ')
        self.assertEqual(reverse_words('a'), 'a')

    def test_boundary_conditions(self):
        self.assertEqual(reverse_words(' ' * 10000 + 'a'), 'a ' + ' ' * 10000)

    def test_more_complex_cases(self):
        self.assertEqual(reverse_words('one two   three'), 'three two one')
        self.assertEqual(reverse_words('1 2 3 4 5'), '5 4 3 2 1')

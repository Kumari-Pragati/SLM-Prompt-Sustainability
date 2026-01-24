import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_edge_cases(self):
        self.assertEqual(multiple_split(''), [])
        self.assertEqual(multiple_split('no_delimiters'), ['no_delimiters'])

    def test_boundary_conditions(self):
        self.assertEqual(multiple_split(';;;'), ['', '', ''])
        self.assertEqual(multiple_split(',,,'), ['', '', ''])
        self.assertEqual(multiple_split('**'), [''])
        self.assertEqual(multiple_split('\n\n\n'), ['', '', ''])

    def test_corner_cases(self):
        self.assertEqual(multiple_split(' ,*; \n'), ['', '', '', '', ''])
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

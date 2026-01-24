import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(multiple_split('a;b,c*d\ne'), ['a', 'b', 'c', '*', 'd', '\n', 'e'])
        self.assertListEqual(multiple_split('a,b,c'), ['a', 'b', 'c'])
        self.assertListEqual(multiple_split('a*b\nc'), ['a', 'b', '\n', 'c'])

    def test_edge_input(self):
        self.assertListEqual(multiple_split(''), [])
        self.assertListEqual(multiple_split(';'), [''])
        self.assertListEqual(multiple_split(';a'), ['', 'a'])
        self.assertListEqual(multiple_split('a,*'), ['a', ''])
        self.assertListEqual(multiple_split('a,*b'), ['a', '', 'b'])
        self.assertListEqual(multiple_split('a,*b,*'), ['a', '', 'b', ''])
        self.assertListEqual(multiple_split('a,*b,*c'), ['a', '', 'b', '', 'c'])

    def test_complex_input(self):
        self.assertListEqual(multiple_split('a;b,c*d\ne;f,g'), ['a', 'b', 'c', '*', 'd', '\n', 'e', ';', 'f', ',', 'g'])
        self.assertListEqual(multiple_split('a,*b,*c,*d'), ['a', '', 'b', '', 'c', '', 'd'])
        self.assertListEqual(multiple_split('a,*b,*c,*d,*'), ['a', '', 'b', '', 'c', '', 'd', '*'])

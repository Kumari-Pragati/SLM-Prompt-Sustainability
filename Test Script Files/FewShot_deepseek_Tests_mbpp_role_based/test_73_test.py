import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_edge_condition(self):
        self.assertEqual(multiple_split(''), [])

    def test_boundary_condition(self):
        self.assertEqual(multiple_split('a'), ['a'])
        self.assertEqual(multiple_split('a;b,c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiple_split(123)

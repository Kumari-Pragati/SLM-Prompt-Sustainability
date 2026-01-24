import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_list_to_float(self):
        self.assertEqual(list_to_float([('1', '2'), ('3', '4')]), "[(1.0, 2.0), (3.0, 4.0)]")
        self.assertEqual(list_to_float([('a', 'b'), ('c', 'd')]), "[(a, b)]")
        self.assertEqual(list_to_float([('1', 'a'), ('b', 'c')]), "[(1.0, a), (b, c)]")
        self.assertEqual(list_to_float([('1', '2', '3'), ('4', '5', '6')]), "[(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]")
        self.assertEqual(list_to_float([('a', 'b', 'c'), ('d', 'e', 'f')]), "[(a, b, c), (d, e, f)]")
        self.assertEqual(list_to_float([]), "[]")
        self.assertEqual(list_to_float([('1',), ('2',)]), "[(1.0,), (2.0,)]")
        self.assertEqual(list_to_float([('a',), ('b',)]), "[(a,), (b,)]")
        self.assertEqual(list_to_float([('1', '2',), ('3', '4',)]), "[(1.0, 2.0,), (3.0, 4.0,)]")
        self.assertEqual(list_to_float([('a', 'b',), ('c', 'd',)]), "[(a, b,), (c, d,)]")

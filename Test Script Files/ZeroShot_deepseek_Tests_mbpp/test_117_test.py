import unittest
from mbpp_117_code import list_to_float

class TestListToFloat(unittest.TestCase):

    def test_list_to_float(self):
        self.assertEqual(list_to_float([('1', '2'), ('3', '4')]), '[(1.0, 2.0), (3.0, 4.0)]')
        self.assertEqual(list_to_float([('a', 'b'), ('c', 'd')]), "[('a', 'b'), ('c', 'd')]")
        self.assertEqual(list_to_float([('1.2', '3.4'), ('5.6', '7.8')]), '[(1.2, 3.4), (5.6, 7.8)]')
        self.assertEqual(list_to_float([('1a', '2b'), ('3c', '4d')]), "[('1a', '2b'), ('3c', '4d')]")

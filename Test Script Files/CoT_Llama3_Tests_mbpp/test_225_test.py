import unittest
from mbpp_225_code import find_Min

class TestFind_Min(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_Min([1,2,3,4,5],0,4), 4)

    def test_edge_low(self):
        self.assertEqual(find_Min([1,1,1,1,1],0,4), 1)

    def test_edge_high(self):
        self.assertEqual(find_Min([1,2,3,4,5],0,0), 1)

    def test_edge_equal(self):
        self.assertEqual(find_Min([1,1,1,1,1],0,4), 1)

    def test_invalid_low(self):
        with self.assertRaises(IndexError):
            find_Min([1,2,3,4,5],5,4)

    def test_invalid_high(self):
        with self.assertRaises(IndexError):
            find_Min([1,2,3,4,5],0,-1)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            find_Min([],0,0)

    def test_single_element(self):
        self.assertEqual(find_Min([1],0,0), 1)

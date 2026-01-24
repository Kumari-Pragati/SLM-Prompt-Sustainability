import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_find_function(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(10, 4), 2)
        self.assertEqual(find(10, 5), 0)
        self.assertEqual(find(10, 10), 0)
        self.assertEqual(find(0, 5), 0)
        self.assertEqual(find(-10, 5), -1)
        self.assertEqual(find(10, 0), 10)

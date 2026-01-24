import unittest
from mbpp_114_code import Counter
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_assign_freq(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 3, 3]), 
                         str([(1, 2), (2, 2), (3, 2)]))
        self.assertEqual(assign_freq(['a', 'a', 'b', 'b', 'c', 'c']), 
                         str([('a', 2), ('b', 2), ('c', 2)]))
        self.assertEqual(assign_freq([1, 'a', 1, 'a', 2, 2]), 
                         str([(1, 2), ('a', 2), (2, 2)]))
        self.assertEqual(assign_freq([]), str([]))

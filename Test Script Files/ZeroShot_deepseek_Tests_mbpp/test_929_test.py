import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_count_tuplex(self):
        self.assertEqual(count_tuplex((1, 2, 3, 4, 5), 3), 1)
        self.assertEqual(count_tuplex((1, 2, 3, 3, 4, 5), 3), 2)
        self.assertEqual(count_tuplex((), 3), 0)
        self.assertEqual(count_tuplex((1, 2, 3, 4, 5), 6), 0)

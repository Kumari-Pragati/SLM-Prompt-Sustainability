import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_increment_numerics(self):
        self.assertEqual(increment_numerics(['a', '1', '2', 'b', '3'], 2), ['a', '3', '4', 'b', '5'])
        self.assertEqual(increment_numerics(['1', '2', '3', '4', '5'], 1), ['2', '3', '4', '5', '6'])
        self.assertEqual(increment_numerics(['a', 'b', 'c', 'd', 'e'], 0), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(increment_numerics(['9', '8', '7', '6', '5'], 5), ['14', '13', '12', '11', '10'])
        self.assertEqual(increment_numerics(['10', '20', '30', '40', '50'], 10), ['20', '30', '40', '50', '60'])

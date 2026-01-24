import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_increment_numerics(self):
        self.assertEqual(increment_numerics([1, 2, 3], 2), ['3', '4', '5'])
        self.assertEqual(increment_numerics(['a', 'b', 1, 2, 3], 2), ['a', 'b', '3', '4', '5'])
        self.assertEqual(increment_numerics([1.5, 2.5, 3.5], 2), ['3.5', '4.5', '5.5'])
        self.assertEqual(increment_numerics(['a', 'b', 'c', 'd', 'e'], 2), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(increment_numerics([1, 2, 3, 4, 5], 0), ['1', '2', '3', '4', '5'])
        self.assertEqual(increment_numerics(['a', 'b', 'c', 'd', 'e'], 0), ['a', 'b', 'c', 'd', 'e'])

    def test_increment_numerics_empty_list(self):
        self.assertEqual(increment_numerics([], 2), [])

    def test_increment_numerics_single_element(self):
        self.assertEqual(increment_numerics([1], 2), ['3'])

    def test_increment_numerics_non_numeric_element(self):
        self.assertEqual(increment_numerics(['a'], 2), ['a'])

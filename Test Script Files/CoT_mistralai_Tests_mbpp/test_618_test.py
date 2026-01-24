import unittest
from mbpp_618_code import map
from six.moves import range
from collections import Iterable

from div_list import div_list

class TestDivList(unittest.TestCase):

    def test_div_list_positive(self):
        self.assertListEqual(div_list([1, 2, 3, 4], [2, 2, 2, 2]), [0.5, 1.0, 0.5, 1.0])
        self.assertListEqual(div_list([5, 10, 15], [2, 2, 3]), [2.5, 5.0, 5.0])
        self.assertListEqual(div_list([], []), [])
        self.assertListEqual(div_list([1], [1]), [1.0])
        self.assertListEqual(div_list([1, 2, 3], []), [Traceback(...)])
        self.assertListEqual(div_list([], [1, 2, 3]), [Traceback(...)])

    def test_div_list_zero_division(self):
        self.assertRaises(ZeroDivisionError, div_list, [1, 0])
        self.assertRaises(ZeroDivisionError, div_list, [0, 1])

    def test_div_list_invalid_inputs(self):
        self.assertRaises(TypeError, div_list, 'a', 'b')
        self.assertRaises(TypeError, div_list, [1, 2, 3], 4)
        self.assertRaises(TypeError, div_list, [1, 2, 3], (1, 2, 3))
        self.assertRaises(TypeError, div_list, [1, 2, 3], {'a': 1, 'b': 2})

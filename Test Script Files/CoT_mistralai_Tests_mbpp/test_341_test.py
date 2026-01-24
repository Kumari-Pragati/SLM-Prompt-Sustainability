import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_empty_set(self):
        self.assertEqual(set_to_tuple({}), ())

    def test_single_element_set(self):
        for element in [1, 'a', 3.14]:
            self.assertEqual(set_to_tuple({element}), (element,))

    def test_multiple_elements_set(self):
        test_set = {1, 'a', 3.14, 1, 'a', 3.14, 'z'}
        sorted_set = sorted(test_set)
        self.assertEqual(set_to_tuple(test_set), tuple(sorted_set))

    def test_duplicate_elements_set(self):
        test_set = {1, 'a', 3.14, 1, 'a', 3.14, 'z', 3.14}
        sorted_set = sorted(test_set)
        self.assertEqual(set_to_tuple(test_set), tuple(sorted_set))

    def test_mixed_types_set(self):
        test_set = {1, 'a', 3.14, [1, 2, 3], (1, 2, 3), {'a', 'b', 'c'}}
        sorted_set = sorted(test_set)
        self.assertEqual(set_to_tuple(test_set), tuple(sorted_set))

    def test_set_with_none(self):
        test_set = {None}
        self.assertEqual(set_to_tuple(test_set), (None,))

    def test_set_with_frozenset(self):
        test_set = {frozenset([1, 2, 3])}
        self.assertEqual(set_to_tuple(test_set), (frozenset([1, 2, 3]),))

    def test_set_with_function(self):
        def test_func():
            pass

        test_set = {test_func}
        self.assertEqual(set_to_tuple(test_set), (<function test_func at 0x...>,))

import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_empty_tuple(self):
        test_tup = ()
        self.assertEqual(clear_tuple(test_tup), ())

    def test_single_element_tuple(self):
        test_tup = (1,)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_large_tuple(self):
        test_tup = tuple(range(1, 1001))
        self.assertEqual(clear_tuple(test_tup), ())

    def test_tuple_with_duplicates(self):
        test_tup = (1, 2, 2, 3, 3, 1)
        self.assertEqual(clear_tuple(test_tup), ())

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            clear_tuple("not a tuple")

import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(tuple_to_dict(()), {})

    def test_single_element_input(self):
        self.assertEqual(tuple_to_dict((1,)), {})

    def test_even_length_input(self):
        self.assertEqual(tuple_to_dict((1, 2, 3, 4)), {1: 2, 3: 4})

    def test_odd_length_input(self):
        self.assertEqual(tuple_to_dict((1, 2, 3, 4, 5)), {1: 2, 3: 4})

    def test_non_integer_values(self):
        self.assertEqual(tuple_to_dict(("a", "b", "c", "d")), {"a": "b", "c": "d"})

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_dict("")

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            tuple_to_dict(None)

import unittest
from mbpp_945_code import tuple_to_set

class TestTupleToSet(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_to_set(()), set)
        self.assertEqual(len(tuple_to_set(())), 0)

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_to_set((1,)), set)
        self.assertEqual(len(tuple_to_set((1,))), 1)
        self.assertIn(1, tuple_to_set((1,)))

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(tuple_to_set((1, 2, 3)), set)
        self.assertEqual(len(tuple_to_set((1, 2, 3))), 3)
        self.assertIn(1, tuple_to_set((1, 2, 3)))
        self.assertIn(2, tuple_to_set((1, 2, 3)))
        self.assertIn(3, tuple_to_set((1, 2, 3)))

    def test_duplicate_elements_tuple(self):
        self.assertIsInstance(tuple_to_set((1, 1, 2, 2, 3)), set)
        self.assertEqual(len(tuple_to_set((1, 1, 2, 2, 3))), 3)
        self.assertIn(1, tuple_to_set((1, 1, 2, 2, 3)))
        self.assertIn(2, tuple_to_set((1, 1, 2, 2, 3)))
        self.assertIn(3, tuple_to_set((1, 1, 2, 2, 3)))

    def test_mixed_types_tuple(self):
        self.assertRaises(TypeError, tuple_to_set, (1, 'a', [1, 2, 3]))

    def test_none_type_tuple(self):
        self.assertRaises(TypeError, tuple_to_set, (None,))

    def test_empty_list_converted_to_tuple(self):
        self.assertIsInstance(tuple_to_set([]), set)
        self.assertEqual(len(tuple_to_set([])), 0)

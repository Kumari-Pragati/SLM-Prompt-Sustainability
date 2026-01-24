import unittest
from mbpp_553_code import tuple_to_float

class TestTupleToFloat(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_to_float([]), float)
        self.assertEqual(tuple_to_float([]), 0.0)

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_to_float((1)), float)
        self.assertEqual(tuple_to_float((1)), 1.0)

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(tuple_to_float((1, 2, 3)), float)
        self.assertEqual(tuple_to_float((1, 2, 3)), 1.0 + 2.0 + 3.0)

    def test_negative_numbers(self):
        self.assertIsInstance(tuple_to_float((-1, 2, -3)), float)
        self.assertEqual(tuple_to_float((-1, 2, -3)), (-1.0 + 2.0 - 3.0))

    def test_floats(self):
        self.assertIsInstance(tuple_to_float((1.1, 2.2, 3.3)), float)
        self.assertEqual(tuple_to_float((1.1, 2.2, 3.3)), 1.1 + 2.2 + 3.3)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            tuple_to_float((1, '2', 3.0))

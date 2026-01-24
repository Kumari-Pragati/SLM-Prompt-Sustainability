import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(rear_extract([1, 2, 3]), [3])
        self.assertEqual(rear_extract([10, 20, 30]), [30])
        self.assertEqual(rear_extract(['a', 'b', 'c']), ['c'])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rear_extract([]), [])
        self.assertEqual(rear_extract([1]), [1])
        self.assertEqual(rear_extract([1, 2]), [2])
        self.assertEqual(rear_extract([1, 2, 3, 4, 5]), [5])
        self.assertEqual(rear_extract([10, 20, 30, 40, 50]), [50])
        self.assertEqual(rear_extract(['a', 'b']), ['b'])
        self.assertEqual(rear_extract(['a', 'b', 'c', 'd']), ['d'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rear_extract(123)
        with self.assertRaises(TypeError):
            rear_extract((1, 2, 3))
        with self.assertRaises(TypeError):
            rear_extract({'a': 1, 'b': 2})

import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 4)
        self.assertEqual(kth_element([-1, -2, -3, -4, -5], 5, 3), -3)
        self.assertEqual(kth_element([10, 20, 30, 40, 50], 5, 3), 30)

    def test_edge_and_boundary(self):
        self.assertEqual(kth_element([1], 1, 1), 1)
        self.assertEqual(kth_element([1], 1, 2), 1)
        self.assertEqual(kth_element([1], 1, 3), TraceError)
        self.assertEqual(kth_element([1], 0, 1), TraceError)
        self.assertEqual(kth_element([1], 2, 1), TraceError)
        self.assertEqual(kth_element([1], 2, 2), 1)

        self.assertEqual(kth_element([1], 5, 1), TraceError)
        self.assertEqual(kth_element([1], 5, 2), TraceError)
        self.assertEqual(kth_element([1], 5, 3), TraceError)
        self.assertEqual(kth_element([1], 5, 4), 1)
        self.assertEqual(kth_element([1], 5, 5), 1)

        self.assertEqual(kth_element([1], 0, 1), TraceError)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, kth_element, [1], 'n', 1)
        self.assertRaises(TypeError, kth_element, [1], n=1, k=1)
        self.assertRaises(TypeError, kth_element, [1], n=1, k='k')

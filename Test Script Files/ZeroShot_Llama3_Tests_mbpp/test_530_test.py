import unittest
from mbpp_530_code import negative_count

class TestNegativeCount(unittest.TestCase):

    def test_negative_count(self):
        self.assertEqual(negative_count(array('i', [1, 2, 3, 4, 5])), 0.0)
        self.assertEqual(negative_count(array('i', [-1, -2, -3, -4, -5])), 1.0)
        self.assertEqual(negative_count(array('i', [1, -2, 3, -4, 5])), 0.4)
        self.assertEqual(negative_count(array('i', [1, 2, 3, -4, 5])), 0.2)
        self.assertEqual(negative_count(array('i', [1, 2, 3, 4, 5, -6])), 0.16666666666666666)
        self.assertEqual(negative_count(array('i', [1, -2, 3, -4, 5, -6])), 0.5)

    def test_empty_array(self):
        self.assertEqual(negative_count(array('i', [])), 0.0)

    def test_single_element_array(self):
        self.assertEqual(negative_count(array('i', [1])), 0.0)
        self.assertEqual(negative_count(array('i', [-1])), 1.0)

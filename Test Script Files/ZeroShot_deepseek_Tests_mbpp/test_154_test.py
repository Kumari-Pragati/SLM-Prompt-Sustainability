import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_specified_element(self):
        self.assertEqual(specified_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])
        self.assertEqual(specified_element([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 2), [30, 60, 90])
        self.assertEqual(specified_element([[100, 200, 300], [400, 500, 600], [700, 800, 900]], 0), [100, 400, 700])
        self.assertEqual(specified_element([], 0), [])
        self.assertRaises(IndexError, specified_element, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3)

import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(add_str([1, 2], 3), [1, 2, 3])

    def test_edge1(self):
        self.assertEqual(add_str([1], 3), [1, 3])

    def test_edge2(self):
        self.assertEqual(add_str([1, 2, 3], 3), [1, 2, 3, 3])

    def test_edge3(self):
        self.assertEqual(add_str([], 3), [3])

    def test_edge4(self):
        self.assertEqual(add_str([1, 2], 0), [1, 2, 0])

    def test_edge5(self):
        self.assertEqual(add_str([1, 2], None), [1, 2, None])

    def test_edge6(self):
        self.assertEqual(add_str([1, 2], '3'), [1, 2, '3'])

    def test_edge7(self):
        self.assertEqual(add_str([1, 2], [3, 4]), [1, 2, [3, 4]])

    def test_edge8(self):
        self.assertEqual(add_str([1, 2], {'3': 4}), [1, 2, {'3': 4}])

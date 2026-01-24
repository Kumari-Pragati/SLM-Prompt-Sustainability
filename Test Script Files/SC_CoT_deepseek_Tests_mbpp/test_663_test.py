import unittest
from mbpp_663_code import find_max_val

class TestFindMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_max_val(10, 2, 0), 10)

    def test_edge_case(self):
        self.assertEqual(find_max_val(0, 1, 0), 0)
        self.assertEqual(find_max_val(10, 1, 1), -1)

    def test_boundary_case(self):
        self.assertEqual(find_max_val(sys.maxsize, 1, 0), sys.maxsize)
        self.assertEqual(find_max_val(sys.maxsize, sys.maxsize, sys.maxsize), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_max_val('10', 2, 0)
        with self.assertRaises(TypeError):
            find_max_val(10, '2', 0)
        with self.assertRaises(TypeError):
            find_max_val(10, 2, '0')

import unittest
from mbpp_578_code import interleave_lists

class TestInterleaveLists(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 4, 7, 2, 5, 8, 3, 9])

    def test_empty(self):
        self.assertEqual(interleave_lists([], [], []), [])

    def test_single_list(self):
        self.assertEqual(interleave_lists([1, 2, 3], [], []), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(interleave_lists([1, 2, 3], [4], [5, 6, 7]), [1, 4, 5, 2, 6, 7, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            interleave_lists(1, 2, 3)

    def test_long_input(self):
        long_list1 = [i for i in range(100)]
        long_list2 = [i for i in range(100, 200)]
        long_list3 = [i for i in range(200, 300)]
        self.assertEqual(len(interleave_lists(long_list1, long_list2, long_list3)), 300)

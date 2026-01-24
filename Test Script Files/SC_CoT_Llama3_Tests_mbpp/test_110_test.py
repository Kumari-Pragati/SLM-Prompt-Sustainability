import unittest
from mbpp_110_code import extract_missing

class TestExtractMissing(unittest.TestCase):
    def test_typical_inputs(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 0
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_edge_cases(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 1
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])

    def test_boundary_cases(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 3
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [(3, 4), (4, 5), (5, 6)])

    def test_special_cases(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 2
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [(2, 3), (3, 4), (4, 5), (5, 6)])

    def test_invalid_inputs(self):
        test_list = [(1, 2), (3, 4), (5, 6)]
        strt_val = 'a'
        stop_val = 6
        with self.assertRaises(TypeError):
            extract_missing(test_list, strt_val, stop_val)

    def test_empty_list(self):
        test_list = []
        strt_val = 0
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [])

    def test_single_element_list(self):
        test_list = [(1, 2)]
        strt_val = 0
        stop_val = 6
        result = extract_missing(test_list, strt_val, stop_val)
        self.assertEqual(result, [(0, 1)])

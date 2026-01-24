import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(count_variable('papap', 'qqqq', 'rrr', 'sss'), ['p', 'q', 'r', 's'])

    def test_edge_case_single_element(self):
        self.assertListEqual(count_variable('p', '', 'r', 's'), ['p', 'r', 's'])

    def test_edge_case_no_elements(self):
        self.assertListEqual(count_variable('', '', '', ''), [])

    def test_edge_case_duplicate_elements(self):
        self.assertListEqual(count_variable('pppp', 'qqqq', 'rrr', 'sss'), ['p', 'q', 'r', 's'])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2, 3, 4)

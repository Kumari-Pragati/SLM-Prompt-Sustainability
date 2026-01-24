import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(start_withp(["Pete is a programmer.", "John is a developer."]), ('Pete', 'programmer'))

    def test_edge_case_empty_list(self):
        self.assertIsNone(start_withp([]))

    def test_edge_case_single_element_list(self):
        self.assertIsNone(start_withp(["Pete is a programmer."]))

    def test_edge_case_single_element_list_no_match(self):
        self.assertIsNone(start_withp(["John is a developer."]))

    def test_edge_case_single_element_list_no_match_no_space(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group_no_capture(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group_no_capture_no_match(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group_no_capture_no_match_no_capture(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group_no_capture_no_match_no_capture_no_group(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

    def test_edge_case_single_element_list_no_match_no_space_no_p_no_w_no_group_no_capture_no_match_no_capture_no_group_no_capture(self):
        self.assertIsNone(start_withp(["Johnisadeveloper."]))

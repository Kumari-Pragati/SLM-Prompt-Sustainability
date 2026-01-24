import unittest
from mbpp_305_code import start_withp

class TestStartWithp(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(start_withp(["Pete is a programmer"]), ('Pete', 'programmer'))

    def test_edge_case_empty_list(self):
        self.assertEqual(start_withp([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(start_withp(["Pete"]), None)

    def test_edge_case_single_element_list_with_match(self):
        self.assertEqual(start_withp(["Pete is a programmer."]), ('Pete', 'programmer'))

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(start_withp(["Pete is a programmer", "John is a teacher"]), ('Pete', 'programmer'))

    def test_edge_case_multiple_elements_list_with_no_match(self):
        self.assertEqual(start_withp(["John is a teacher", "Mary is a student"]), None)

    def test_edge_case_multiple_elements_list_with_multiple_matches(self):
        self.assertEqual(start_withp(["Pete is a programmer", "John is a teacher", "Pete is a developer"]), ('Pete', 'programmer'))

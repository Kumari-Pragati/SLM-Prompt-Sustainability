import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_uppercase('HelloWorld'), 'elloorld')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_uppercase(''), '')

    def test_boundary_case_all_uppercase(self):
        self.assertEqual(remove_uppercase('HELLO'), 'ello')

    def test_corner_case_mixed_case(self):
        self.assertEqual(remove_uppercase('hElLO'), 'ello')

    def test_corner_case_numbers_and_uppercase(self):
        self.assertEqual(remove_uppercase('He12LL0'), 'ello')

    def test_corner_case_special_characters_and_uppercase(self):
        self.assertEqual(remove_uppercase('H@W!O'), '@!o')

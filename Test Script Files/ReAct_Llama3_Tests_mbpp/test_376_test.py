import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_replica((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))

    def test_edge_case(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3, 3)), ('MSP', 'MSP', 2, 2, 3, 3))

    def test_empty_input(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element_input(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_duplicates_and_non_duplicates(self):
        self.assertEqual(remove_replica((1, 2, 2, 3, 4, 5, 5)), (1, 2, 3, 4, 5))

    def test_duplicates_and_non_duplicates_with_msp(self):
        self.assertEqual(remove_replica((1, 2, 2, 3, 4, 5, 5, 5)), ('MSP', 1, 2, 3, 4, 5))

    def test_duplicates_and_non_duplicates_with_msp_and_empty(self):
        self.assertEqual(remove_replica(()), ())

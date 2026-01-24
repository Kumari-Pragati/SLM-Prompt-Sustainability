import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_remove_unique_elements(self):
        self.assertEqual(remove_replica((1, 2, 3, 4)), (1, 2, 3, 4))

    def test_remove_duplicate_elements(self):
        self.assertEqual(remove_replica((1, 1, 2, 3)), (1, 2, 3))

    def test_empty_tuple(self):
        self.assertEqual(remove_replica(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_single_element_in_set(self):
        self.assertEqual(remove_replica((1, 1)), ('MSP',))

    def test_repeated_single_element_in_set(self):
        self.assertEqual(remove_replica((1, 1, 1)), ('MSP',))

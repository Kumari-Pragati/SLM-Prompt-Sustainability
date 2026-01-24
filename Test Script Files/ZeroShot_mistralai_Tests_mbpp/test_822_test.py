import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(pass_validity("Ab123456"))
        self.assertTrue(pass_validity("Ab12345678"))
        self.assertTrue(pass_validity("Ab1234567890"))
        self.assertTrue(pass_validity("Ab1234567890Z"))
        self.assertTrue(pass_validity("Ab1234567890#"))
        self.assertTrue(pass_validity("Ab1234567890@"))
        self.assertTrue(pass_validity("Ab1234567890$"))
        self.assertTrue(pass_validity("Ab1234567890%"))
        self.assertTrue(pass_validity("Ab1234567890&"))
        self.assertTrue(pass_validity("Ab1234567890*"))
        self.assertTrue(pass_validity("Ab1234567890-"))
        self.assertTrue(pass_validity("Ab1234567890_"))
        self.assertTrue(pass_validity("Ab1234567890+"))
        self.assertTrue(pass_validity("Ab1234567890="))
        self.assertTrue(pass_validity("Ab1234567890!"))
        self.assertTrue(pass_validity("Ab1234567890~"))

    def test_invalid_password_length(self):
        self.assertFalse(pass_validity("a"))
        self.assertFalse(pass_validity("abcd"))
        self.assertFalse(pass_validity("abcdefg"))
        self.assertFalse(pass_validity("abcdefghij"))
        self.assertFalse(pass_validity("abcdefghijkl"))
        self.assertFalse(pass_validity("abcdefghijklm"))
        self.assertFalse(pass_validity("abcdefghijklmnop"))
        self.assertFalse(pass_validity("abcdefghijklmnopq"))
        self.assertFalse(pass_validity("abcdefghijklmnopqr"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrs"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrst"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstu"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuv"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvw"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxy"))
        self.assertFalse(pass_validity("abcdefghijklmnopqrstuvwxyz"))

    def test_invalid_no_lowercase(self):
        self.assertFalse(pass_validity("ABC123456"))
        self.assertFalse(pass_validity("ABC12345678"))
        self.assertFalse(pass_validity("ABC1234567890"))
        self.assertFalse(pass_validity("ABC1234567890Z"))
        self.assertFalse(pass_validity("ABC1234567890#"))
        self.assertFalse(pass_validity("ABC1234567890@"))
        self.assertFalse(pass_validity("ABC1234567890$"))
        self.assertFalse(pass_validity("ABC1234567890%"))
        self.assertFalse(pass_validity("ABC1234567890
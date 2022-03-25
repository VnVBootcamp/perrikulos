"""Unit test file for perrikulos.py"""
from app import perrikulos.returnBackwardsString
import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for perrikulos.py"""

    def test_return_backwards_string(self):
        """Test return backwards simple string"""
        random_string = "Perrikulos"
        random_string_reversed = "solukirreP"
        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))

if __name__ == "__main__":
    unittest.main()
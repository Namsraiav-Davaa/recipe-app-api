"""
    Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test case calc module."""

    def test_add_numbers(self):
        """test adding two numbers. """
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        """Test subtract numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
""" 
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc Module"""

    def test_add_the_numbers(self):
        """Test adding the numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_the_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

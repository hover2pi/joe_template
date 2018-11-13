"""This module contains a variety of tests for the module.py module"""
import unittest

from joe_template import MyClass

 
class TestStuff(unittest.TestCase):
    """Tests for MyClass class"""
    def setUp(self):
        pass

    def test_myclass(self):
        """Test if Filter object is created properly"""
        # Comments are nice too
        words = 'Here are the words!'
        mc = MyClass(words)

        # Here's another
        self.assertTrue(mc.words == 'Here are the words!')

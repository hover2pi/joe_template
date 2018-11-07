"""This is a sample module with a nice docstring that Sphinx will pick up"""
import numpy as np


class MyClass:
    """The classes have docstrings"""
    def __init__(self, words):
        """And the functions and methods have them too
        
        Parameters
        ----------
        words: str
            The words
        """
        self.words = words

"""Parser mixin class for any paresr to implement"""
from typing import Dict
from typing import List


class Parser:
    """class for Parser interface"""

    def __init__(self):
        self._data: List[Dict] = []

    def read(self, files: List[str]):
        """stub for a parsers method that reads in a list of files given their paths"""

    @property
    def data(self) -> List[Dict]:
        """a computed instance attribute to protect data from changing by external code"""
        return self._data

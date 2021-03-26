"""Code responsible for providing XML parsing functionality"""
import logging
import os
from typing import Dict
from typing import List

import xmltodict

from tr.parsers.parser import Parser

logger = logging.getLogger(__name__)

__all__ = [
    'XMLParser'
]


class XMLParser(Parser):
    """class That handles parsing XML files"""

    def read(self, files: List[str]):
        """
        takes in a list of xml files and parses them into python dicts, sets the Parser data field

        :param List[str] files: a list of file paths to read
        :return: None, results are in the data property
        """

        for path in files:
            if os.path.exists(path):
                try:
                    with open(path, 'r') as xml_file:
                        data = {'file_name': path}
                        data.update(xmltodict.parse(xml_file.read()))
                        self._data.append(self.format_data(data))
                # deliberately catching any possible exception ans skipping, disabling pylint warning
                except Exception as ex:  # pylint: disable=broad-except
                    logger.error("Couldn't parse xml file %s , moving on...", path, exc_info=ex)
            else:
                logger.error("Couldn't find xml file %s , moving on...", path)

    @classmethod
    def format_data(cls, data: Dict):
        """
        cleans input dict key and returns clean version

        :param data: dict to clean
        :return: clean dict
        """
        cleaned_data = {}
        data_copy = data.copy()
        if 'Transaction' in data_copy:
            data_copy['Transaction']['vehicles'] = data['Transaction']['Customer']['Units']['Vehicle']
            del data_copy['Transaction']['Customer']['Units']
        for key in data_copy:
            clean_key = key.lower().replace('@', '')
            clean_key = clean_key if clean_key != 'vinnumber' else 'vin_number'
            if isinstance(data_copy[key], list):
                cleaned_data[clean_key] = data_copy[key]
                for i, item in enumerate(cleaned_data[clean_key]):
                    if isinstance(item, dict):
                        cleaned_data[clean_key][i] = cls.format_data(item)
            if isinstance(data_copy[key], dict):
                cleaned_data[clean_key] = cls.format_data(data_copy[key])
            else:
                cleaned_data[clean_key] = data_copy[key]

        return cleaned_data

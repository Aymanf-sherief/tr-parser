import json
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from tr.parsers.xml_parser import XMLParser


class TestXMLParser(unittest.TestCase):

    @patch('os.path.exists')
    @patch('tr.parsers.xml_parser.open')
    def test_read(self, mock_open: MagicMock, mock_exists: MagicMock):
        mock_exists.return_value = True
        mock_read = MagicMock()
        mock_read.return_value = r"""<?xml version="1.0" encoding="UTF-8"?>
                                        <Transaction>
                                            <Date>2020-10-15</Date>
                                            <Customer id="ID1011601">
                                                <Name>Aleena Chan</Name>
                                                <Address>3344 Joy Lane</Address>
                                                <Phone>818-537-1995</Phone>
                                                <Units>
                                                    <Vehicle id="V1000">
                                                        <Make>Nissan</Make>
                                                        <VinNumber>JA32V6FV2DU023115</VinNumber>
                                                    </Vehicle>
                                                    <Vehicle id="V1001">
                                                        <Make>Toyota</Make>
                                                        <VinNumber>1FUJGLDR2DLB61105</VinNumber>
                                                    </Vehicle>
                                                </Units>
                                            </Customer>
                                        </Transaction>
"""
        mock_open.return_value.__enter__.return_value = MagicMock(read=mock_read)
        parser = XMLParser()
        parser.read(['xml/customer2.xml'])
        expected_data = {
            "file_name": "xml/customer2.xml",
            "transaction": {
                "date": "2020-10-15",
                "customer": {
                    "id": "ID1011601",
                    "name": "Aleena Chan",
                    "address": "3344 Joy Lane",
                    "phone": "818-537-1995"
                },
                "vehicles": [
                    {
                        "id": "V1000",
                        "make": "Nissan",
                        "vin_number": "JA32V6FV2DU023115"
                    },
                    {
                        "id": "V1001",
                        "make": "Toyota",
                        "vin_number": "1FUJGLDR2DLB61105"
                    }
                ]
            }
        }

        actual_data = parser.data[0]
        self.assertEqual(json.dumps(expected_data), json.dumps(actual_data))

import json
import unittest
from io import StringIO
from unittest.mock import MagicMock
from unittest.mock import patch

from tr.parsers.csv_parser import CSVParser


class TestXMLParser(unittest.TestCase):

    @patch('os.path.exists')
    @patch('tr.parsers.csv_parser.open')
    def test_read(self, mock_open: MagicMock, mock_exists: MagicMock):
        mock_exists.return_value = True
        mock_open.return_value.__enter__.side_effect = [StringIO("""
"id","name","address","phone","date"
"ID5410","Melissa T Miller","2837  Fidler Drive","210-624-7306","31/01/2020"
"ID9857","Daniel I Walker","3853  Hilltop Street","413-655-7397","25/04/2020"
""".strip()),
StringIO(r"""
"id","make","vin_number","owner_id"
"V3015","Chevrolet","1HGFA16548L016469","ID9857"
"V2014","Honda","1G6KD57Y46U180996","ID9857"
"V1475","Ford","2HKYF18575H574967","ID5410"
""".strip())]
        parser = CSVParser()
        parser.read(('csv/customers.csv', 'csv/vehicles.csv'))
        expected_data = [{
            "file_name": "csv/customers.csv",
            "transaction": {
                "date": "31/01/2020",
                "customer": {
                    "id": "ID5410",
                    "name": "Melissa T Miller",
                    "address": "2837  Fidler Drive",
                    "phone": "210-624-7306"
                },
                "vehicles": [
                    {
                        "id": "V1475",
                        "make": "Ford",
                        "vin_number": "2HKYF18575H574967"
                    }]
            }
        }, {
            "file_name": "csv/customers.csv",
            "transaction": {
                "date": "25/04/2020",
                "customer": {
                    "id": "ID9857",
                    "name": "Daniel I Walker",
                    "address": "3853  Hilltop Street",
                    "phone": "413-655-7397"
                },
                "vehicles": [
                    {
                        "id": "V3015",
                        "make": "Chevrolet",
                        "vin_number": "1HGFA16548L016469"
                    },
                    {
                        "id": "V2014",
                        "make": "Honda",
                        "vin_number": "1G6KD57Y46U180996"
                    }
                ]
            }
        }
        ]

        actual_data = parser.data
        self.assertEqual(json.dumps(expected_data), json.dumps(actual_data))

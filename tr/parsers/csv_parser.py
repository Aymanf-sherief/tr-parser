"""Code responsible for providing CSV parsing functionality"""
import csv
import logging
import os
from itertools import groupby
from typing import Tuple

from tr.parsers.parser import Parser

logger = logging.getLogger(__name__)


class CSVParser(Parser):
    """class That handles parsing CSV files"""

    def read(self, files: Tuple[str, str]):
        """
        takes in a tuple [customers_csv_path, vehicles_csv_path] and parses it into python dicts,
         sets the Parser data field

        :param Tuple[str] files: a tuple of the two required files
        :return: None, results are in the data property
        """
        for path in files:
            if not os.path.exists(path):
                raise ValueError(f"Couldn't find csv file {path}")

        with open(files[0], encoding='utf-8') as customers_csv:
            customers = list(csv.DictReader(customers_csv))
            for i, c in enumerate(customers):
                transaction = {'date': c.pop('date'), 'customer': c}
                new_c = {'file_name': files[0], 'transaction': transaction}
                customers[i] = new_c
        with open(files[1], encoding='utf-8') as vehicles_csv:
            vehicles = list(csv.DictReader(vehicles_csv))

        customers = sorted(customers, key=lambda c: (c['transaction']['customer']['id']))
        vehicles = sorted(vehicles, key=lambda v: (v['owner_id']))
        for owner_index, (_, vehicle_group) in enumerate(groupby(vehicles, key=lambda v: v['owner_id'])):
            customer_vehicles = []
            for v in vehicle_group:
                del v['owner_id']
                customer_vehicles.append(v)

            customers[owner_index]['transaction']['vehicles'] = customer_vehicles

        self._data = customers

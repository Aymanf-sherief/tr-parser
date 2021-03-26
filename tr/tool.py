import json
import logging
from typing import List
from typing import Tuple

import typer

from tr.parsers.csv_parser import CSVParser
from tr.parsers.xml_parser import XMLParser

logger = logging.getLogger(__name__)
parser_tool = typer.Typer()


@parser_tool.command("xml")
def xml_to_json(files: List[str], output_file: str = typer.Option('customers.json', "-o", "--out",
                                                                  help="The output json file path"),
                formatted: bool = typer.Option(False, '-f', "--format", help="whether to format json output")):
    """
    converts xml files to json

    :param files: list of file paths to convert
    :param output_file: optional output file path, if not passed the default is customers.json
    :param formatted: whether to format json output
    """
    logger.info("converting files %s from xml to json", files)
    invalid_files = []
    for file in files:
        if not file.endswith('xml'):
            invalid_files.append(file)
    if invalid_files:
        logger.warning("Files %s have an unsupported extension, the tool will attempt converting...", invalid_files)

    parser = XMLParser()
    parser.read(files)

    with open(output_file, 'w') as f:
        if formatted:
            json.dump(parser.data, f, indent=4)
        else:
            json.dump(parser.data, f)
    logger.info("wrote json data to %s", output_file)


@parser_tool.command("csv")
def csv_to_json(files: Tuple[str, str], output_file: str = typer.Option('customers.json', "-o", "--out",
                                                                        help="The output json file path"),
                formatted: bool = typer.Option(False, '-f', "--format", help="whether to format json output")):
    """
    converts xml files to json

    :param files: list of file paths to convert
    :param output_file: optional output file path, if not passed the default is customers.json
    :param formatted: whether to format json output
    """
    logger.info("converting files %s from csv to json", files)
    invalid_files = []
    for file in files:
        if not file.endswith('csv'):
            invalid_files.append(file)
    if invalid_files:
        logger.warning("Files %s have an unsupported extension, the tool will attempt converting...", invalid_files)

    parser = CSVParser()
    parser.read(files)
    with open(output_file, 'w') as f:
        if formatted:
            json.dump(parser.data, f, indent=4)
        else:
            json.dump(parser.data, f)

    logger.info("wrote json data to %s", output_file)


if __name__ == '__main__':
    parser_tool()

# tr-parser
A parser for xml \ csv customer transaction data that can convert them to a unified json format

# How to install

1. clone the repository
2. run `python setup.py install`

Please note:
- you might need to use a shell with administrator privileges
- the tool will be available as a CLI command `tr-parser`
- if you don't want to install the tool to use it,
  you can run the same commands without installing
  by replacing `tr-parser` with `tr\tool.py` after installing required packages

- even though the task requested that the tool would run with the command `parser.py`,
  I've renamed the file to `tool.py` to avoid confusion with the [parser](https://docs.python.org/3/library/parser.html)
  module, and instead provided the tool as an installable CLI tool

# Usage

the CLI is built using [typer](https://typer.tiangolo.com/), so when in doubt, you can always try `tr-parser --help`

- #### The tool supports converting xml files to json using
  Please note that the default output path will be `customers.json` in the current working directory
  
  - single file: `tr-parser xml xml/customer1.xml`
  - multiple files: `tr-parser xml xml/customer1.xml xml/customer2.xml`
  - format json output: `tr-parser xml xml/customer1.xml -f`
  - specify output json path: `tr-parser xml xml/customer1.xml -o customer1.json`
  - or just see what's available `tr-parser xml --help`
    

- #### The tool supports converting csv files to json using
  Please note:
  1. the default output path will be `customers.json` in the current working directory
  2. the tool expectes the files in the order `customers.csv`, `vehicles.csv`
  - convert csv files: `tr-parser csv csv/customers.csv csv/vehicles.csv` 
  - format json output: `tr-parser csv csv/customers.csv csv/vehicles.csv -f`
  - specify output json path: `tr-parser csv csv/customers.csv csv/vehicles.csv -o other_customers.json`
  - or just see what's available `tr-parser csv --help`
    
# Possible improvements
- Batch mode: the ability to take a directory as input, convert all csv, xml files in it to a single json output file

    

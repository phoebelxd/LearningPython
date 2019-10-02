# Learning Python

Some basic python scripts for TRGN 510 [Basic Foundations in Translational Biomedical Informatics](https://www.bioinform.io/site/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

[Python 3](https://www.python.org/download/releases/3.0/) required. I personally recommend [PyCharm](https://www.jetbrains.com/pycharm/).

## Deployment

part 1

Create a basic python script called circumference.py, and output the circumference of a circle of radius 3 following 2*pi*r, pi = 3.14159.

```python
pi = 3.14159

radius = 3

print("The circumference of a circle of radius 3 is " + str (pi * radius * 2.0))
```

part 2

Create a basic python script called areaCode.py for printing out the area code 602 for the phone number "602-343-8747".

```python
import re
phone = "602-343-8747"
print("The area code is: " + re.match(r"^[0-9]*", phone).group())
```

part 3

Download the file, Homo_sapiens.GRCh37.75.gtf.gz, from http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens and place this file within a directory called data. 

Create a python script called gene_names.py, and output a list of data under specific order using JSON format.

```python
import sys # Load in module that accesses the command line
import fileinput # This module gives us the ability to read files
import re # This imports the regex capability
my_file= sys.argv[1] # Assign my_file to whatever was argument 1
print("[")
for each_line_of_text in fileinput.input(my_file):
    if re.match(r'.*\t.*\tgene\t', each_line_of_text):
        gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
        if gene_name_matches:
            result = re.match(r"(\w*)\t\w*\t\w*\t(\w*)\t(\w*)\t", each_line_of_text)
            print ('{"geneName":"'+gene_name_matches[0]+'","chr":"'+result. group(1)+'","startPos":'+result. group(2)+', "endPos":'+result. group(3)+'},')
print("]")
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [David Wesley Craig, PhD](https://keck.usc.edu/faculty-search/david-wesley-craig/)



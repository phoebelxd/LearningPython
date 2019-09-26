#!/usr/bin/python
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
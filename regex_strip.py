#! /usr/local/bin/python3

import re


def regex_strip(string, replace_pattern):
    if len(replace_pattern) != 0:
        pattern = r'[' + replace_pattern + r']+'

        strip_regex = re.compile(pattern)
        string = strip_regex.sub('', string)
    else:
        pattern = re.compile(r'^\s*')
        strip_regex = re.compile(pattern)
        string = strip_regex.sub('', string)

        pattern = re.compile(r'\s*$')
        strip_regex = re.compile(pattern)
        string = strip_regex.sub('', string)

    return string


print(regex_strip("Hello whats up", 'lap'))
print(regex_strip("    My Name is     ", ''))

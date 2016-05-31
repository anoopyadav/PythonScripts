#! /usr/local/bin/python3
# Scans the text on the clipboard for phone numbers and emails, copies them back

import re
import pyperclip


def find_phone_numbers(text):
    phone_regex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?      # Area code
                            (-|\.|\s)?              # Separator
                            (\d{3})                 # First three digits
                            (-|\.|\s)?              # Separator
                            (\d{4})                 # Last four digits
                            )''', re.VERBOSE)

    matches = []

    for groups in phone_regex.findall(text):
        phone_number = '-'.join([groups[1], groups[3], groups[5]]).replace('(', '').replace(')', '')

        # strip leading - in case no area code
        phone_number = phone_number.lstrip('-')
        matches.append(phone_number)

    return matches


def find_email(text):
    email_regex = re.compile('''(
                            ([\w\.]+)           # Email name
                            @                   # The @ symbol
                            (\w)+               # Domain name
                            .                   # The .
                            ([a-zA-Z]{2,4})     # .SOMETHING
                            )''', re.VERBOSE)

    matches = []
    for groups in email_regex.findall(text):
        matches.append(groups[0])

    return matches


clipboard_text = str(pyperclip.paste())

phone_numbers = find_phone_numbers(clipboard_text)

emails = find_email(clipboard_text)

matches = phone_numbers + emails

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found!')

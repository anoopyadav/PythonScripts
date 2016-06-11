#! /usr/local/bin/python3

# Rules: Minimum 8 alphanumeric characters, mixed case and atleast 1 digit

import re


# ?= is the lookahead assertion, it only return whether a match is possible, otherwise returns None
# ?! is the negative lookahead
def detect_strength(password_string):
    result = "Acceptable password!"

    if len(password_string) < 8:
        return "Password must be atleast 8 characters!"

    if re.search(r'(?=[A-Z]+)', password_string) is None:
        return 'Need at least one uppercase character'

    if re.search(r'(?=[a-z]+)', password_string) is None:
        return 'Need at least one lowercase character'

    if re.search(r'(?=[0-9]+)', password_string) is None:
        return 'Need at least one numeric character'

    return result


print(detect_strength('password'))
print(detect_strength('Password'))
print(detect_strength('Password1'))

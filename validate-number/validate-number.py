"""
"123" True
"-1.23" True
"abc" False
"1.1.1" False
"1,000" False
".54" True
"1a" False
"+234" False
"1." True
"1-1" False
".5 4" False
" .54 " False
"" False
"-" False
"." False
"""


def isValidNumber(s):
    if not s or (len(s) == 1 and not s.isdigit()):
        return False

    has_decimal = False

    for idx, char in enumerate(s):
        if char == '-':
            if idx != 0:
                return False
        elif char == '.':
            if has_decimal:
                return False
            has_decimal = True
        elif not char.isdigit():
            return False

    return True


strings = [
    "123",
    "-1.23",
    "abc",
    "1.1.1",
    "1,000",
    ".54",
    "1a",
    "+234",
    "1.",
    "1-1",
    ".5 4",
    " .54 ",
    "",
    "-",
    ".",
]

for s in strings:
    print(isValidNumber(s))

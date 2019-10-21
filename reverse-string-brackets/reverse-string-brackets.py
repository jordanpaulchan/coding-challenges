"""
Given a string with valid brackets (could have multiple nested brackets), 
reverse the contents of the brackets and return the string with the reversed 
content and no brackets
"""


def reverseChars(chars, left, right):
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverseStringBrackets(string):
    if not string:
        return ''

    chars = list(string)
    stack = []
    for idx, char in enumerate(chars):
        if char == '(':
            stack.append(idx)
        elif char == ')':
            left = stack.pop()
            reverseChars(chars, left + 1, idx - 1)

    return ''.join(filter(lambda s: s not in {'(', ')'}, chars))


print(reverseStringBrackets('(Hello)World'))
print(reverseStringBrackets('World(Hello)'))
print(reverseStringBrackets('((HelloWorld))'))
print(reverseStringBrackets('(HelloWorld)'))
print(reverseStringBrackets('(Hello)(World)'))
print(reverseStringBrackets('(Hello(World)Good)'))

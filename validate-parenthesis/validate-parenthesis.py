def validate_parenthesis(input):
    stack = []
    temp = input
    for idx, char in enumerate(temp):
        if char == '(':
            stack.append((char, idx))
        elif char == ')':
            if stack and stack[-1][0] == '(':
                # remove from input
                stack.pop()
            else:
                stack.append((char, idx))

    # Valid input
    if not stack:
        return input

    ans = []
    remove = set([idx for char, idx in stack])
    for idx, char in enumerate(input):
        if idx not in remove:
            ans.append(char)

    return ''.join(ans)


print(validate_parenthesis('()'))
print(validate_parenthesis('())())'))
print(validate_parenthesis('())))'))
print(validate_parenthesis('().(()'))
print(validate_parenthesis(')'))
print(validate_parenthesis('((()'))

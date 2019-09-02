#
# Complete the 'validate_xml' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING xml as parameter.
#


def get_tag(xml, idx):
    tag = ''
    next_idx = idx + 1
    while xml[next_idx] != '>' or next_idx >= len(xml):
        if next_idx >= len(xml) or xml[next_idx] == '<':
            return '', next_idx

        tag += xml[next_idx]
        next_idx += 1

    return tag, next_idx + 1


def validate_xml(xml):
    # Write your code here
    stack = []
    idx = 0
    while idx < len(xml):
        if xml[idx] == '<':
            if idx + 1 >= len(xml):
                return 'parse error'
            elif xml[idx + 1] == '/':
                closing_tag, next_idx = get_tag(xml, idx + 1)
                if not closing_tag:
                    return 'parse error'
                elif not stack or stack[-1] != closing_tag:
                    return 'encountered closing tag without matching open tag for </{}>'.format(closing_tag)
                else:
                    stack.pop()
            else:
                opening_tag, next_idx = get_tag(xml, idx)
                if not opening_tag:
                    return 'parse error'
                stack.append(opening_tag)
            idx = next_idx
        else:
            idx += 1

    if stack:
        return 'missing closing tag for <{}>'.format(stack[-1])

    return 'valid'


if __name__ == '__main__':
    print(validate_xml('<invalid<>text</invalid>'))

"""
Input:
      6
     / \
    3   4
   / \   \
  5   1   0
   \     /
    2   8
   / \
  9   7

Output: 5 9 3 2 6 1 7 4 8 0
"""


def printColumns(root):
    if not root:
        return

    queue = [(root, 0)]
    columns = {}

    while queue:
        tempq = []
        for node, column in queue:
            if column not in columns:
                columns[column] = []
            columns[column].append(node.val)

            if node.left:
                tempq.append((node.left, column - 1))

            if node.right:
                tempq.append((node.right, column + 1))

        queue = tempq

    ans = []
    for column in sorted(columns.keys()):
        ans.extend(columns[column])
    print(ans)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nine = Node(9)
seven = Node(7)
two = Node(2, nine, seven)
five = Node(5, None, two)
one = Node(1)
three = Node(3, five, one)
eight = Node(8)
zero = Node(0, eight)
four = Node(4, None, zero)
six = Node(6, three, four)

printColumns(six)

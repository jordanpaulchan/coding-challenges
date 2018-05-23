# Ancestors

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for “earliest”, return any one of them. If the input individual has no parents, the function should return null (or -1).

## Example

1 2 4
\ / / \
 3 5 8
\ / \ \
 6 7 9

### Input:

[
[1, 3],
[2, 3],
[3, 6],
[5, 6],
[5, 7],
[4, 5],
[4, 8],
[8, 9]
];

### Output:

8 => 4
7 => 4
6 => 1, 2, or 4

## Run the program

In the folder run the command:

```
node ancestors.js
```

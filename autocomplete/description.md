# Trie

We're going to make our own autocomplete application! The application must perform two types of operations:

1.  Add word. This must store the word as a new entry in the application.
2.  Get words. A string denoting a partial word to search the application for. It must find all of the words it is a prefix for and return them in a list.

Given n sequential add and get operations, perform each operation in order.

## Example

### Input:

add boat
add goat
add booking
get bo
get goat

### Output:

boat, booking
goat

## Run the program

In the folder run the command:

```
python autocomplete.py
```

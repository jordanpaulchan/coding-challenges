# Hungry rabbit

There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0.
Each element of a matrix is an integer representing points gained for being on the spot.
If there are multiple possible "middles" then choose the one which has the highest point value to start on.
On each iteration, the rabbit can move up, left, right, or down.
The rabbit will always move to the next spot with the highest point value and will "consume" those points (set the point value in that position to 0).
The rabbit spots when all positions around it are 0s. Calculate how many points the rabbit will score for a given m x n matrix.

## Example

### Input

5, 7, 8, 6, 3
0, 0, 7, 0, 4
4, 6, 3, 4, 9
3, 1, 0, 5, 8

### Output

27

## Run the program

In the folder run the command:

```
python hungry-rabbit.py
```

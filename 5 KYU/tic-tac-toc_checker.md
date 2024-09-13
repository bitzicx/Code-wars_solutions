
# Description 
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's 
current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty, `1` if it is an "X", or `2` if it is an "O", like so:

```
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

- `-1` if the board is not yet finished AND no one has won yet (there are empty spots),
- `1` if "X" won,
- `2` if "O" won,
- `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

So this is simple kata, Simple in a sense that its easy to understand what the question really wants. 
So there is different ways, One of the way that always comes to our mind is brute force method, Going one by one through each row and checking them, the other is using loops, its also in a type of brute force but at least we are not breaking the keyboard by typing so much. 

### Solution using python

```
def is_solved(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != 0:
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    for row in board:
        for cell in row:
            if cell == 0:
                return -1
    return 0
```
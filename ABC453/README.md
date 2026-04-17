# ABC453

## C - Sneaking Glances

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 300 points

### Problem Statement

Takahashi is at coordinate 0.5 on a number line. He will make N moves. In the i-th move, he chooses either the positive direction or the negative direction, and moves L_i in that direction. What is the maximum number of times he can pass through coordinate 0?

Under the constraints of this problem, no move will end at coordinate 0.

### Constraints

- 1 ≤ N ≤ 20
- 1 ≤ L_i ≤ 10^9
- All input values are integers.

### Input

```
N L_1 L_2 … L_N
```

### Output

Output the answer.

### Sample Input 1

```
5 2 5 2 2 1
```

### Sample Output 1

```
4
```

For example, by choosing the directions of movement as follows, he can pass through coordinate 0 four times, which is the maximum.
- In the first move, choose the negative direction and move 2. He moves from coordinate 0.5 to -1.5, passing through coordinate 0.
- In the second move, choose the positive direction and move 5. He moves from coordinate -1.5 to 3.5, passing through coordinate 0.
- In the third move, choose the negative direction and move 2. He moves from coordinate 3.5 to 1.5.
- In the fourth move, choose the negative direction and move 2. He moves from coordinate 1.5 to -0.5, passing through coordinate 0.
- In the fifth move, choose the positive direction and move 1. He moves from coordinate -0.5 to 0.5, passing through coordinate 0.

---

## D - Go Straight

**Time Limit**: 2 sec / **Memory Limit**: 1024 MiB  
**Score**: 425 points

### Problem Statement

There is a grid of H rows × W columns, and Takahashi moves through this grid up, down, left, and right.

The state of the cell at the i-th row from the top and j-th column from the left (1 ≤ i ≤ H, 1 ≤ j ≤ W) is represented by the character S_{i,j}.

S_{i,j} is one of `#`, `.`, `o`, `x`, `S`, `G`.

- If S_{i,j} = `#`: This cell cannot be entered.
- If S_{i,j} = `.`: This cell can be freely entered and exited. After entering this cell, Takahashi can move to any adjacent cell (if it exists).
- If S_{i,j} = `o`: In this cell, **Takahashi must move in the same direction as the immediately preceding move**. After entering this cell, he must move to the next cell without changing direction.
- If S_{i,j} = `x`: In this cell, **Takahashi cannot move in the same direction as the immediately preceding move**. After entering this cell, he must change direction to move to the next cell. Turning 180 degrees to return to the previous cell is considered as changing direction.
- If S_{i,j} = `S`: This cell is Takahashi's starting position. This cell can be freely entered and exited.
- If S_{i,j} = `G`: This cell is Takahashi's destination. This cell can be freely entered and exited.

There is exactly one `S` and exactly one `G` in the grid.

Takahashi wants to reach the destination by repeatedly moving to adjacent cells from his starting position. Determine whether this is possible, and if so, output one valid sequence of moves with at most 5 × 10^6 moves. It is not necessary to minimize the number of moves.

### Constraints

- 1 ≤ H, W ≤ 1000
- S_{i,j} is one of `#`, `.`, `o`, `x`, `S`, `G`.
- There is exactly one `S` and exactly one `G`.

### Input

```
H W
S_{1,1} S_{1,2} … S_{1,W}
S_{2,1} S_{2,2} … S_{2,W}
⋮
S_{H,1} S_{H,2} … S_{H,W}
```

### Output

If impossible, output `No` on the first line, and nothing on the second line.

If possible, output `Yes` on the first line. On the second line, output a string T representing the sequence of moves. T must satisfy:
- Length |T| is between 1 and 5 × 10^6, inclusive.
- Each character is one of `U`, `D`, `L`, `R`.
- Takahashi is never outside the grid after any move.
- The conditions of each cell are not violated during the moves.
- After the |T|-th move, Takahashi is at the destination cell.

### Sample Input 1

```
3 5
.#...
.Sooo
..x.G
```

### Sample Output 1

```
Yes
DRUUDDRR
```

### Sample Input 2

```
3 3
#So
xoG
..#
```

### Sample Output 2

```
Yes
DDLURR
```

### Sample Input 3

```
2 2
So
oG
```

### Sample Output 3

```
No
```
